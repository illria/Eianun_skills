# Bcut Subtitle Extractor CLI Reference

## Default command

Generate the two normal outputs from the newest Bcut draft:

```bash
python scripts/extract_bcut_subtitles.py --drafts-dir "~/Movies/Bcut Drafts"
```

Default outputs:

- `extracted_subtitles.source.srt`: original aligned source SRT, no cleanup, no merge.
- `extracted_subtitles.enhanced.srt`: enhanced SRT with the same block boundaries/timestamps as the source SRT, plus punctuation/filler cleanup.

This is the intended everyday workflow. Do not add `--clean --write-source` for the default task; those behaviors are already enabled by default. Do not add `--smart-segment` unless the user explicitly asks to repair split fragments.

## Specific project

```bash
python scripts/extract_bcut_subtitles.py \
  --project "/Users/wenruo/Movies/Bcut Drafts/PROJECT_NAME"
```

Specify the enhanced output path:

```bash
python scripts/extract_bcut_subtitles.py \
  --project "/Users/wenruo/Movies/Bcut Drafts/PROJECT_NAME" \
  --output "/Users/wenruo/Desktop/extracted_subtitles.enhanced.srt"
```

The source SRT will be written beside it as:

```text
/Users/wenruo/Desktop/extracted_subtitles.enhanced.source.srt
```

Choose exact source path:

```bash
python scripts/extract_bcut_subtitles.py \
  --project "/Users/wenruo/Movies/Bcut Drafts/PROJECT_NAME" \
  --output "/Users/wenruo/Desktop/extracted_subtitles.enhanced.srt" \
  --source-output "/Users/wenruo/Desktop/extracted_subtitles.source.srt"
```

## Troubleshooting commands

List recent projects:

```bash
python scripts/extract_bcut_subtitles.py --drafts-dir "~/Movies/Bcut Drafts" --list-projects
```

Debug extraction:

```bash
python scripts/extract_bcut_subtitles.py \
  --project "/Users/wenruo/Movies/Bcut Drafts/PROJECT_NAME" \
  --debug \
  --json-report "/Users/wenruo/Desktop/bcut-subtitles-report.json"
```

Search a known subtitle line manually:

```bash
grep -R -a -n "一条真实字幕内容" "~/Movies/Bcut Drafts"
```

## Options

Core options:

- `--drafts-dir PATH`: Bcut drafts directory. Defaults to `~/Movies/Bcut Drafts`.
- `--project PATH`: Specific project folder or `.json` / `.bjson` file. If omitted, the newest project is used.
- `--output PATH`, `-o PATH`: Enhanced output SRT path. If omitted, writes `extracted_subtitles.enhanced.srt` in the project folder.
- `--source-output PATH`: Source SRT path. If omitted, writes `extracted_subtitles.source.srt` for default project output, or `<output-stem>.source.srt` when `--output` is provided.
- `--list-projects`: List recent projects and exit.
- `--json-report PATH`: Write a JSON debug report of extracted subtitle entries.
- `--debug`: Print extraction diagnostics.

Mode options, only for unusual cases:

- `--enhanced-only`: Write only the enhanced clean SRT and skip the source SRT.
- `--source-only`: Write only the original aligned source SRT and skip the enhanced SRT.
- `--clean`: Explicit shortcut for `--strip-punctuation --strip-fillers`. Default already uses these for enhanced output. It does not enable smart merging.
- `--write-source`: Explicitly write the source SRT. Default already writes it.

Cleanup options:

- `--strip-punctuation`: Remove comma, exclamation, and period punctuation from caption text. Required SRT timestamp commas are preserved.
- `--punctuation-chars CHARS`: Override removed punctuation characters. Default: `,，.!！。`.
- `--strip-fillers`: Remove common口语 filler words such as `啊`, `嗯`, `哦`, `噢`, `喔`, `呃`, `额`, `诶`, `欸`, `哎`, `唉`, `呀`, `呐`, `呢`. Also removes standalone English fillers `um`, `uh`, `er`, `ah`.
- `--filler-words WORDS`: Override Chinese filler words. Accepts comma/space separated values, for example `--filler-words "啊,嗯,哦,呃,额,呢"`.

Smart segmentation options, only for explicit split-fragment repair:

- `--smart-segment`: Conservatively merge tiny ASR fragments. Not enabled by default because preserving the original Bcut screen density is usually better for video.
- `--max-chars N`: Hard maximum characters per subtitle screen. Default: `22`.
- `--min-chars N`: Minimum characters before a soft break is allowed. Default: `6`.
- `--max-duration SECONDS`: Hard maximum subtitle-screen duration. Default: `3.2`.
- `--max-gap SECONDS`: Maximum gap between raw captions that may be merged. Default: `0.35`.
