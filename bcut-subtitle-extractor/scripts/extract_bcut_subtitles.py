#!/usr/bin/env python3
"""Extract subtitles from Bcut/Bilibili video editor draft files and write SRT.

This script is intentionally schema-tolerant. Bcut draft files may appear as
.json or .bjson and may store captions either directly on timeline segments or
as text materials referenced by segment material IDs.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple

TEXT_KEYS = (
    "text",
    "content",
    "caption",
    "captionText",
    "subtitle",
    "sentence",
    "word",
    "words",
    "recognition_text",
    "recognize_text",
    "initial_text",
    "plain_text",
)
ID_KEYS = ("id", "material_id", "text_id", "ref_id", "resource_id")
TEXT_PATH_HINTS = (
    "text",
    "texts",
    "caption",
    "captions",
    "subtitle",
    "subtitles",
    "asr",
    "recogn",
    "sentence",
    "words",
    "materials",
)
TIME_RANGE_KEYS = (
    "target_timerange",
    "source_timerange",
    "render_timerange",
    "timerange",
    "time_range",
    "range",
)

DEFAULT_STRIP_PUNCTUATION = ",，.!！。"
DEFAULT_FILLER_WORDS = (
    "啊", "嗯", "哦", "噢", "喔", "呃", "额", "诶", "欸", "哎", "唉", "呀", "呐", "呢"
)
UNSAFE_END_TOKENS = (
    "的", "地", "得", "了", "着", "过", "和", "与", "或", "及", "跟",
    "在", "对", "把", "被", "给", "从", "到", "向", "比", "为",
    "是", "有", "将", "会", "要", "能", "可", "很", "更", "最",
    "就", "都", "也", "还", "又", "再", "并", "而", "但", "让",
    "一个", "这个", "那个", "如果", "因为", "所以", "但是", "而且", "然后", "以及",
)
UNSAFE_START_TOKENS = (
    "的", "地", "得", "了", "着", "过", "吗", "呢", "吧", "啊", "呀",
    "么", "们", "里", "上", "下", "中", "后", "前", "就", "都", "也", "还",
)
SENTENCE_END_PUNCTUATION = "。.!！?？"

@dataclass
class Subtitle:
    start: float
    end: float
    text: str
    source: str


def eprint(*args: object) -> None:
    print(*args, file=sys.stderr)


def expand_path(p: str) -> Path:
    return Path(os.path.expandvars(os.path.expanduser(p))).resolve()


def file_mtime_safe(path: Path) -> float:
    try:
        return path.stat().st_mtime
    except OSError:
        return 0.0


def project_score(path: Path) -> float:
    if path.is_file():
        return file_mtime_safe(path)
    best = file_mtime_safe(path)
    for f in path.rglob("*"):
        if f.is_file():
            best = max(best, file_mtime_safe(f))
    return best


def find_latest_project(drafts_dir: Path) -> Path:
    if not drafts_dir.exists():
        raise FileNotFoundError(f"drafts directory not found: {drafts_dir}")
    children = [p for p in drafts_dir.iterdir() if not p.name.startswith(".")]
    dirs = [p for p in children if p.is_dir()]
    if dirs:
        return max(dirs, key=project_score)
    files = [p for p in children if p.is_file() and p.suffix.lower() in {".json", ".bjson"}]
    if files:
        return max(files, key=file_mtime_safe)
    raise FileNotFoundError(f"no project folders or json/bjson files found in: {drafts_dir}")


def list_projects(drafts_dir: Path, limit: int = 10) -> List[Tuple[Path, float]]:
    if not drafts_dir.exists():
        raise FileNotFoundError(f"drafts directory not found: {drafts_dir}")
    items = [p for p in drafts_dir.iterdir() if not p.name.startswith(".")]
    items = [p for p in items if p.is_dir() or p.suffix.lower() in {".json", ".bjson"}]
    return sorted(((p, project_score(p)) for p in items), key=lambda x: x[1], reverse=True)[:limit]


def read_text_lossy(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    for enc in ("utf-8", "utf-8-sig", "gb18030", "utf-16", "utf-16-le", "utf-16-be"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8", errors="ignore")


def load_jsonish(path: Path) -> Optional[Any]:
    text = read_text_lossy(path)
    text = text.strip("\x00\ufeff\n\r\t ")
    if not text:
        return None
    try:
        return json.loads(text)
    except Exception:
        pass
    # Some bjson files include non-json bytes before/after the JSON payload.
    first_obj = min([i for i in [text.find("{"), text.find("[")] if i >= 0], default=-1)
    last_obj = max(text.rfind("}"), text.rfind("]"))
    if first_obj >= 0 and last_obj > first_obj:
        snippet = text[first_obj : last_obj + 1]
        try:
            return json.loads(snippet)
        except Exception:
            return None
    return None


def iter_nodes(obj: Any, path: str = "") -> Iterator[Tuple[str, Any]]:
    yield path, obj
    if isinstance(obj, dict):
        for k, v in obj.items():
            child = f"{path}.{k}" if path else str(k)
            yield from iter_nodes(v, child)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            child = f"{path}[{i}]"
            yield from iter_nodes(v, child)


def path_has_text_hint(path: str) -> bool:
    lower = path.lower()
    return any(h in lower for h in TEXT_PATH_HINTS)


def looks_like_noise(s: str) -> bool:
    if not s:
        return True
    if len(s) > 600:
        return True
    lower = s.lower().strip()
    if lower.startswith(("http://", "https://", "file://")):
        return True
    if re.fullmatch(r"[#a-f0-9\-_:/.]{8,}", lower):
        return True
    if re.fullmatch(r"[\d\s:.,\-_/]+", lower):
        return True
    skip_words = {
        "default",
        "normal",
        "none",
        "left",
        "right",
        "center",
        "bold",
        "italic",
        "regular",
        "sans",
    }
    if lower in skip_words:
        return True
    return False


def strip_markup(s: str) -> str:
    s = html.unescape(s)
    s = s.replace("\\n", "\n").replace("\\N", "\n")
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\{\\[^}]+\}", "", s)
    s = s.replace("\r", "\n")
    s = re.sub(r"[ \t\u00a0]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def extract_text_from_string(s: str) -> str:
    s = s.strip()
    if not s:
        return ""
    # Bcut/Jianying text material often stores a JSON string in content.
    if s[0] in "[{" and s[-1:] in "]}":
        try:
            nested = json.loads(s)
            nested_texts = []
            for p, node in iter_nodes(nested):
                if isinstance(node, str) and p.lower().endswith(tuple(TEXT_KEYS)):
                    cleaned = strip_markup(node)
                    if cleaned and not looks_like_noise(cleaned):
                        nested_texts.append(cleaned)
            if nested_texts:
                return max(nested_texts, key=len)
        except Exception:
            pass
    cleaned = strip_markup(s)
    if looks_like_noise(cleaned):
        return ""
    return cleaned


def text_from_dict(d: Dict[str, Any], path: str = "") -> str:
    candidates: List[str] = []
    for key in TEXT_KEYS:
        if key in d and isinstance(d[key], str):
            t = extract_text_from_string(d[key])
            if t:
                candidates.append(t)
    # Sometimes words are stored as a list of word objects.
    for key in ("words", "tokens", "items"):
        value = d.get(key)
        if isinstance(value, list):
            parts = []
            for item in value:
                if isinstance(item, dict):
                    t = text_from_dict(item, path)
                    if t:
                        parts.append(t)
                elif isinstance(item, str):
                    t = extract_text_from_string(item)
                    if t:
                        parts.append(t)
            joined = "".join(parts) if any(re.search(r"[\u4e00-\u9fff]", p) for p in parts) else " ".join(parts)
            joined = strip_markup(joined)
            if joined and not looks_like_noise(joined):
                candidates.append(joined)
    if not candidates:
        return ""
    # Prefer the longest meaningful field; content JSON tends to include the caption.
    return max(candidates, key=len)


def normalize_time_value(value: Any) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    try:
        n = float(value)
    except (TypeError, ValueError):
        return None
    if n < 0:
        return None
    # Common draft units: microseconds, milliseconds, centiseconds, seconds.
    if n >= 100000:
        return n / 1000000.0
    if n >= 1000:
        return n / 1000.0
    return n


def extract_timerange(d: Dict[str, Any]) -> Optional[Tuple[float, float]]:
    # Bcut caption track entries use inPoint/outPoint in milliseconds, even
    # when values are below 1000. Treat them explicitly instead of guessing.
    if "inPoint" in d and "outPoint" in d:
        try:
            start = float(d["inPoint"]) / 1000.0
            end = float(d["outPoint"]) / 1000.0
        except (TypeError, ValueError):
            start = None
            end = None
        if start is not None and end is not None and end > start:
            return start, end

    # Direct start/end keys.
    start_keys = ("start", "start_time", "startTime", "begin", "begin_time", "from")
    end_keys = ("end", "end_time", "endTime", "stop", "to")
    duration_keys = ("duration", "dur", "length")

    start_raw = next((d.get(k) for k in start_keys if k in d), None)
    end_raw = next((d.get(k) for k in end_keys if k in d), None)
    duration_raw = next((d.get(k) for k in duration_keys if k in d), None)
    start = normalize_time_value(start_raw)
    end = normalize_time_value(end_raw)
    duration = normalize_time_value(duration_raw)
    if start is not None and end is not None and end > start:
        return start, end
    if start is not None and duration is not None and duration > 0:
        return start, start + duration

    # Nested timerange objects.
    for key in TIME_RANGE_KEYS:
        value = d.get(key)
        if isinstance(value, dict):
            tr = extract_timerange(value)
            if tr:
                return tr
    return None


def build_material_text_map(obj: Any) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for path, node in iter_nodes(obj):
        if not isinstance(node, dict):
            continue
        ids = [str(node[k]) for k in ID_KEYS if k in node and isinstance(node[k], (str, int))]
        if not ids:
            continue
        t = text_from_dict(node, path)
        if not t:
            continue
        if not path_has_text_hint(path) and "type" in node:
            typ = str(node.get("type", "")).lower()
            if "text" not in typ and "caption" not in typ and "subtitle" not in typ:
                continue
        for i in ids:
            result.setdefault(i, t)
    return result


def collect_subtitles_from_obj(obj: Any, source_name: str) -> List[Subtitle]:
    subtitles: List[Subtitle] = []
    material_text = build_material_text_map(obj)

    for path, node in iter_nodes(obj):
        if not isinstance(node, dict):
            continue
        tr = extract_timerange(node)
        if not tr:
            continue
        start, end = tr
        if end <= start:
            continue

        text = text_from_dict(node, path)
        if not text:
            for key in ID_KEYS:
                value = node.get(key)
                if isinstance(value, (str, int)):
                    text = material_text.get(str(value), "")
                    if text:
                        break
        if not text:
            continue
        # Avoid pulling media filenames or style labels from non-text timeline segments.
        if not path_has_text_hint(path):
            ids = [str(node.get(k)) for k in ID_KEYS if node.get(k) is not None]
            if not any(i in material_text for i in ids):
                # Keep direct text with obvious content, otherwise skip.
                if not re.search(r"[\u4e00-\u9fffA-Za-z]", text):
                    continue
        subtitles.append(Subtitle(start=start, end=end, text=text, source=source_name))

    return subtitles


def find_draft_files(project: Path) -> List[Path]:
    if project.is_file():
        return [project]
    preferred_names = {
        "draft_content.json",
        "draft_info.json",
        "draftinfo.json",
        "draft_meta_info.json",
        "draft_content.bjson",
        "draft_info.bjson",
    }
    all_files = [p for p in project.rglob("*") if p.is_file() and p.suffix.lower() in {".json", ".bjson"}]
    def rank(p: Path) -> Tuple[int, float]:
        name = p.name.lower()
        preferred = 0 if name in preferred_names or "draft" in name.lower() else 1
        return preferred, -file_mtime_safe(p)
    return sorted(all_files, key=rank)


def dedupe_and_sort(subtitles: Iterable[Subtitle]) -> List[Subtitle]:
    seen = set()
    result: List[Subtitle] = []
    for s in sorted(subtitles, key=lambda x: (x.start, x.end, x.text)):
        text = strip_markup(s.text)
        if not text:
            continue
        # Clamp weird zero-length captions.
        end = s.end if s.end > s.start else s.start + 1.5
        key = (round(s.start, 3), round(end, 3), text)
        if key in seen:
            continue
        seen.add(key)
        result.append(Subtitle(s.start, end, text, s.source))
    return result


def remove_punctuation(text: str, chars: str = DEFAULT_STRIP_PUNCTUATION) -> str:
    """Remove selected punctuation while preserving spacing and line breaks."""
    if not chars:
        return text
    table = str.maketrans("", "", chars)
    text = text.translate(table)
    text = re.sub(r"[ \t\u00a0]+", " ", text)
    return text.strip()


def parse_filler_words(value: str) -> Tuple[str, ...]:
    if not value:
        return tuple()
    parts = re.split(r"[,，\s]+", value.strip())
    return tuple(p for p in parts if p)


def remove_fillers(text: str, filler_words: Tuple[str, ...] = DEFAULT_FILLER_WORDS) -> str:
    """Remove common spoken filler particles from subtitle text.

    Chinese ASR often emits fillers as standalone one-character fragments such as
    啊/嗯/哦/呃/额.  Remove repeated runs conservatively and also remove common
    English fillers only when they are standalone words.
    """
    if not text or not filler_words:
        return text

    # Remove standalone English fillers only on word boundaries.
    text = re.sub(r"\b(?:um+|uh+|er+|ah+)\b", " ", text, flags=re.IGNORECASE)

    # Remove Chinese filler runs, including repeated forms such as 嗯嗯 / 啊啊.
    # Keep this list focused on discourse particles; do not remove content words
    # such as 这个/那个 by default.
    escaped = [re.escape(w) for w in sorted(filler_words, key=len, reverse=True)]
    pattern = r"(?:" + "|".join(escaped) + r")+"
    text = re.sub(pattern, "", text)

    # Clean up spaces and obvious punctuation-only leftovers around removed fillers.
    text = re.sub(r"[ \t\u00a0]+", " ", text)
    text = re.sub(r"^[,，.!！。?？、;；:：\s]+|[,，.!！。?？、;；:：\s]+$", "", text)
    text = re.sub(r"([,，.!！。?？、;；:：]){2,}", r"\1", text)
    return text.strip()


def clean_subtitle_text(
    text: str,
    strip_punctuation: bool = False,
    punctuation_chars: str = DEFAULT_STRIP_PUNCTUATION,
    strip_fillers: bool = False,
    filler_words: Tuple[str, ...] = DEFAULT_FILLER_WORDS,
) -> str:
    text = strip_markup(text)
    if strip_fillers:
        text = remove_fillers(text, filler_words)
    if strip_punctuation:
        text = remove_punctuation(text, punctuation_chars)
    return text.strip()


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def join_caption_text(left: str, right: str) -> str:
    left = left.strip()
    right = right.strip()
    if not left:
        return right
    if not right:
        return left
    if right[0] in "，,。.!！?？、;；:：)）]】」』" or left[-1] in "([{（【「『":
        return left + right
    if re.search(r"[A-Za-z0-9]$", left) and re.search(r"^[A-Za-z0-9]", right):
        return left + " " + right
    if has_cjk(left) or has_cjk(right):
        return left + right
    return left + " " + right


def text_ends_with_any(text: str, tokens: Tuple[str, ...]) -> bool:
    stripped = text.strip()
    return any(stripped.endswith(token) for token in tokens)


def text_starts_with_any(text: str, tokens: Tuple[str, ...]) -> bool:
    stripped = text.strip()
    return any(stripped.startswith(token) for token in tokens)


def safe_to_break_between(left: str, right: str) -> bool:
    """Return False for boundaries likely to split a phrase across subtitle screens."""
    left = left.strip()
    right = right.strip()
    if not left or not right:
        return True
    if left[-1] in SENTENCE_END_PUNCTUATION:
        return True
    if text_ends_with_any(left, UNSAFE_END_TOKENS):
        return False
    if text_starts_with_any(right, UNSAFE_START_TOKENS):
        return False
    # Avoid splitting adjacent Latin words / identifiers such as Open + AI or v2 + ray.
    if re.search(r"[A-Za-z0-9]$", left) and re.search(r"^[A-Za-z0-9]", right):
        return False
    return True


def should_break_group(
    current: Subtitle,
    next_sub: Subtitle,
    max_chars: int,
    min_chars: int,
    max_duration: float,
    max_gap: float,
) -> bool:
    gap = next_sub.start - current.end
    if gap > max_gap:
        return True

    current_text = current.text.strip()
    next_text = next_sub.text.strip()
    current_len = len(re.sub(r"\s+", "", current_text)) if has_cjk(current_text) else len(current_text)
    duration = current.end - current.start
    safe_boundary = safe_to_break_between(current_text, next_text)

    if current_text.endswith(tuple(SENTENCE_END_PUNCTUATION)) and current_len >= min_chars:
        return True
    if current_len < min_chars:
        return False
    if (current_len >= max_chars or duration >= max_duration) and safe_boundary:
        return True

    merged_text = join_caption_text(current_text, next_text)
    merged_len = len(re.sub(r"\s+", "", merged_text)) if has_cjk(merged_text) else len(merged_text)
    merged_duration = next_sub.end - current.start

    # Hard visual limits: never create long subtitle screens. Earlier versions
    # allowed up to about 2x max_chars when a boundary looked unsafe, which made
    # the enhanced SRT fill the whole video frame. Break anyway when limits are
    # exceeded.
    if merged_len > max_chars or merged_duration > max_duration:
        return True

    # At this point the merged screen is still short, so it is OK to repair a
    # likely phrase split by merging.
    if not safe_boundary:
        return False
    return False


def smart_segment_subtitles(
    subtitles: List[Subtitle],
    max_chars: int = 22,
    min_chars: int = 6,
    max_duration: float = 3.2,
    max_gap: float = 0.35,
) -> List[Subtitle]:
    """Conservatively repair tiny ASR fragments without creating subtitle walls.

    This mode is intentionally NOT the default enhanced output. It is only for
    cases where Bcut has split a tiny particle/word into the next subtitle. Keep
    each screen short: never merge past max_chars or max_duration just to avoid
    an awkward grammar boundary.
    """
    if not subtitles:
        return []
    ordered = sorted(subtitles, key=lambda x: (x.start, x.end))
    groups: List[Subtitle] = []
    current = Subtitle(ordered[0].start, ordered[0].end, ordered[0].text.strip(), ordered[0].source)

    for nxt in ordered[1:]:
        nxt_clean = Subtitle(nxt.start, nxt.end, nxt.text.strip(), nxt.source)
        if should_break_group(current, nxt_clean, max_chars, min_chars, max_duration, max_gap):
            groups.append(current)
            current = nxt_clean
        else:
            current = Subtitle(
                current.start,
                max(current.end, nxt_clean.end),
                join_caption_text(current.text, nxt_clean.text),
                current.source if current.source == nxt_clean.source else f"{current.source}; {nxt_clean.source}",
            )
    groups.append(current)
    return groups


def postprocess_subtitles(
    subtitles: List[Subtitle],
    smart_segment: bool = False,
    strip_punctuation: bool = False,
    punctuation_chars: str = DEFAULT_STRIP_PUNCTUATION,
    strip_fillers: bool = False,
    filler_words: Tuple[str, ...] = DEFAULT_FILLER_WORDS,
    max_chars: int = 28,
    min_chars: int = 8,
    max_duration: float = 5.5,
    max_gap: float = 0.8,
) -> List[Subtitle]:
    processed = [
        Subtitle(s.start, s.end, clean_subtitle_text(s.text, False, punctuation_chars, strip_fillers, filler_words), s.source)
        for s in subtitles
    ]
    processed = [s for s in processed if s.text]
    if smart_segment:
        processed = smart_segment_subtitles(processed, max_chars=max_chars, min_chars=min_chars, max_duration=max_duration, max_gap=max_gap)
    if strip_punctuation or strip_fillers:
        processed = [
            Subtitle(s.start, s.end, clean_subtitle_text(s.text, strip_punctuation, punctuation_chars, strip_fillers, filler_words), s.source)
            for s in processed
        ]
        processed = [s for s in processed if s.text]
    return processed


def fmt_ts(seconds: float) -> str:
    if seconds < 0:
        seconds = 0
    ms_total = int(round(seconds * 1000))
    ms = ms_total % 1000
    sec_total = ms_total // 1000
    sec = sec_total % 60
    minutes_total = sec_total // 60
    minute = minutes_total % 60
    hour = minutes_total // 60
    return f"{hour:02d}:{minute:02d}:{sec:02d},{ms:03d}"


def write_srt(subtitles: List[Subtitle], output: Path) -> None:
    lines: List[str] = []
    for idx, s in enumerate(subtitles, 1):
        lines.append(str(idx))
        lines.append(f"{fmt_ts(s.start)} --> {fmt_ts(s.end)}")
        lines.extend(s.text.splitlines() or [s.text])
        lines.append("")
    output.write_text("\n".join(lines), encoding="utf-8")


def write_json_report(subtitles: List[Subtitle], output: Path) -> None:
    output.write_text(json.dumps([asdict(s) for s in subtitles], ensure_ascii=False, indent=2), encoding="utf-8")


def extract_from_project(project: Path, debug: bool = False) -> List[Subtitle]:
    files = find_draft_files(project)
    if not files:
        raise FileNotFoundError(f"no .json or .bjson files found in project: {project}")
    collected: List[Subtitle] = []
    parsed_count = 0
    for f in files:
        obj = load_jsonish(f)
        if obj is None:
            continue
        parsed_count += 1
        subs = collect_subtitles_from_obj(obj, str(f))
        if debug and subs:
            eprint(f"found {len(subs)} subtitle candidates in {f}")
        collected.extend(subs)
    if debug:
        eprint(f"parsed {parsed_count}/{len(files)} json/bjson files")
    return dedupe_and_sort(collected)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="extract the latest Bcut/Bilibili editor subtitles and write SRT")
    parser.add_argument("--drafts-dir", default="~/Movies/Bcut Drafts", help="Bcut drafts directory; default: ~/Movies/Bcut Drafts")
    parser.add_argument("--project", help="specific project folder or .json/.bjson file; default: latest project in drafts-dir")
    parser.add_argument("--output", "-o", help="enhanced output .srt path; default: project-folder/extracted_subtitles.enhanced.srt")
    parser.add_argument("--list-projects", action="store_true", help="list recent projects and exit")
    parser.add_argument("--limit", type=int, default=10, help="number of projects to list with --list-projects")
    parser.add_argument("--json-report", help="optional debug JSON report with extracted subtitle entries")
    parser.add_argument("--clean", action="store_true", help="shortcut for --strip-punctuation --strip-fillers; default behavior already creates a cleaned enhanced SRT without merging screens")
    parser.add_argument("--strip-punctuation", action="store_true", help="remove common comma/exclamation/period punctuation from subtitle text")
    parser.add_argument("--punctuation-chars", default=DEFAULT_STRIP_PUNCTUATION, help=f"punctuation characters removed by --strip-punctuation; default: {DEFAULT_STRIP_PUNCTUATION}")
    parser.add_argument("--strip-fillers", action="store_true", help="remove common spoken filler words such as 啊/嗯/哦/呃/额 from caption text")
    parser.add_argument("--filler-words", default=",".join(DEFAULT_FILLER_WORDS), help="comma/space separated filler words removed by --strip-fillers")
    parser.add_argument("--write-source", action="store_true", help="also write an original aligned SRT before cleanup/smart segmentation; enabled by default unless --enhanced-only is used")
    parser.add_argument("--source-output", help="path for original aligned SRT; implies --write-source")
    parser.add_argument("--enhanced-only", action="store_true", help="write only the enhanced clean SRT and skip the original aligned source SRT")
    parser.add_argument("--source-only", action="store_true", help="write only the original aligned source SRT and skip the enhanced clean SRT")
    parser.add_argument("--smart-segment", action="store_true", help="optional conservative repair for tiny split fragments; not enabled by default because it may change subtitle timing density")
    parser.add_argument("--max-chars", type=int, default=22, help="smart segmentation hard max characters per subtitle screen")
    parser.add_argument("--min-chars", type=int, default=6, help="smart segmentation minimum characters before allowing a soft break")
    parser.add_argument("--max-duration", type=float, default=3.2, help="smart segmentation hard max seconds per subtitle screen")
    parser.add_argument("--max-gap", type=float, default=0.35, help="max seconds between raw captions that smart segmentation may merge")
    parser.add_argument("--debug", action="store_true", help="print extraction diagnostics to stderr")
    args = parser.parse_args(argv)

    drafts_dir = expand_path(args.drafts_dir)

    if args.list_projects:
        for p, ts in list_projects(drafts_dir, args.limit):
            print(f"{int(ts)}\t{p}")
        return 0

    explicit_enhance_flags = args.clean or args.smart_segment or args.strip_punctuation or args.strip_fillers
    default_two_version_mode = not args.source_only and not args.enhanced_only and not explicit_enhance_flags

    # Default workflow for the user's common Bcut task:
    # write two files only:
    # 1) source SRT: original Bcut timing/text alignment
    # 2) enhanced SRT: same timing density, with punctuation/filler cleanup only
    # Do NOT merge screens by default; long merged captions fill the video frame.
    if args.clean or default_two_version_mode or (args.enhanced_only and not explicit_enhance_flags):
        args.strip_punctuation = True
        args.strip_fillers = True

    if default_two_version_mode or (not args.enhanced_only and not args.source_only):
        args.write_source = True

    if args.source_only:
        args.write_source = True
        args.smart_segment = False
        args.strip_punctuation = False
        args.strip_fillers = False

    project = expand_path(args.project) if args.project else find_latest_project(drafts_dir)
    raw_subtitles = extract_from_project(project, debug=args.debug)

    if args.output:
        output = expand_path(args.output)
    else:
        base = project if project.is_dir() else project.parent
        # The default final file is the enhanced version. The unmodified aligned
        # version is written beside it as extracted_subtitles.source.srt.
        output = base / "extracted_subtitles.enhanced.srt"

    if args.source_output:
        args.write_source = True
        source_output = expand_path(args.source_output)
    elif args.output:
        source_output = output.with_name(f"{output.stem}.source{output.suffix}")
    else:
        base = project if project.is_dir() else project.parent
        source_output = base / "extracted_subtitles.source.srt"

    if args.write_source:
        source_output.parent.mkdir(parents=True, exist_ok=True)
        write_srt(raw_subtitles, source_output)

    if args.source_only:
        print(f"ok: wrote {len(raw_subtitles)} source subtitles to {source_output}")
        return 0

    filler_words = parse_filler_words(args.filler_words)
    subtitles = postprocess_subtitles(
        raw_subtitles,
        smart_segment=args.smart_segment,
        strip_punctuation=args.strip_punctuation,
        punctuation_chars=args.punctuation_chars,
        strip_fillers=args.strip_fillers,
        filler_words=filler_words,
        max_chars=args.max_chars,
        min_chars=args.min_chars,
        max_duration=args.max_duration,
        max_gap=args.max_gap,
    )
    if not subtitles:
        eprint("no subtitles found. try --project with the exact draft folder, or inspect with grep -R -a '<one caption line>' '<drafts-dir>'")
        return 2

    output.parent.mkdir(parents=True, exist_ok=True)
    write_srt(subtitles, output)

    if args.json_report:
        write_json_report(subtitles, expand_path(args.json_report))

    if args.write_source:
        print(f"ok: wrote {len(raw_subtitles)} source subtitles to {source_output}")
    print(f"ok: wrote {len(subtitles)} subtitles to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
