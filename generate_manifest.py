#!/usr/bin/env python3
"""掃描 questions_json 目錄並建立 manifest.json。"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PATTERN = re.compile(r"^\d{3}-(?:1|2)-U[12]\.json$", re.IGNORECASE)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "folder",
        nargs="?",
        type=Path,
        default=Path("questions_json"),
        help="題庫資料夾，預設為 questions_json",
    )
    args = parser.parse_args()

    folder: Path = args.folder
    if not folder.is_dir():
        parser.error(f"找不到資料夾：{folder}")

    files = sorted(
        path.name
        for path in folder.glob("*.json")
        if path.name != "manifest.json" and PATTERN.match(path.name)
    )

    output = folder / "manifest.json"
    output.write_text(
        json.dumps({"files": files}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"已建立 {output}，共 {len(files)} 個題庫。")


if __name__ == "__main__":
    main()
