#!/usr/bin/env python3
"""Check final generated thumbnail dimensions and aspect ratio."""
from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("--target-width", type=int, default=1280)
    parser.add_argument("--target-height", type=int, default=720)
    args = parser.parse_args()

    path = Path(args.image)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")
    with Image.open(path) as im:
        width, height = im.size
        ratio = width / height
    target_ratio = args.target_width / args.target_height
    print(f"Image: {path}")
    print(f"Size: {width}x{height}")
    print(f"Aspect ratio: {ratio:.4f}")
    ok = True
    if (width, height) != (args.target_width, args.target_height):
        print(f"WARN: expected {args.target_width}x{args.target_height}")
        ok = False
    if abs(ratio - target_ratio) > 0.01:
        print("WARN: aspect ratio is not close to 16:9")
        ok = False
    if ok:
        print("PASS: size/aspect ratio look correct")
    else:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
