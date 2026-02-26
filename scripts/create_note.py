#!/usr/bin/env python3
"""Create a dated report note path and optional markdown draft."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import sys
import unicodedata
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a docs/notes report file path from a topic."
    )
    parser.add_argument("topic", help="Topic text for the report title and slug.")
    parser.add_argument(
        "--base-dir",
        default="docs/notes",
        help="Output directory relative to the current working directory.",
    )
    parser.add_argument(
        "--date",
        help="Override date in YYYY-MM-DD format. Defaults to today's local date.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the target path without writing a file.",
    )
    return parser.parse_args()


def date_text(raw: str | None) -> str:
    if raw:
        try:
            dt.date.fromisoformat(raw)
        except ValueError as exc:
            raise ValueError("--date must be YYYY-MM-DD") from exc
        return raw
    return dt.date.today().isoformat()


def topic_slug(topic: str) -> str:
    normalized = unicodedata.normalize("NFKD", topic).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized).strip("-").lower()
    if slug:
        return slug[:70].rstrip("-")
    digest = hashlib.sha1(topic.encode("utf-8")).hexdigest()[:8]
    return f"topic-{digest}"


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    for index in range(2, 1000):
        candidate = path.with_name(f"{stem}-{index}{suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError("Could not allocate unique filename after 999 attempts")


def default_body(topic: str, date_iso: str, repo_root: Path) -> str:
    return f"""# {topic} investigation report

- Created on: {date_iso}
- Topic: {topic}
- Target repository: `{repo_root}`

## TL;DR
- 

## Topic and scope
- 

## Method (where and how I investigated)
- Local investigation:
- External investigation:

## Findings (with evidence)
### 1. 
- Fact:
- Evidence:

## Impact / implications
- 

## Open questions and risks
- 

## Recommended next actions
1. 
2. 

## Sources
| Type | Path/URL | Key Points |
| --- | --- | --- |
"""


def main() -> int:
    args = parse_args()
    base_dir = Path.cwd() / args.base_dir
    date_iso = date_text(args.date)
    slug = topic_slug(args.topic)
    target = unique_path(base_dir / f"{date_iso}_{slug}.md")

    if args.dry_run:
        print(str(target))
        return 0

    base_dir.mkdir(parents=True, exist_ok=True)
    target.write_text(default_body(args.topic, date_iso, Path.cwd()), encoding="utf-8")
    print(str(target))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
