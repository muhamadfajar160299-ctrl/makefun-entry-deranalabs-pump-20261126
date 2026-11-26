#!/usr/bin/env python3
"""deranalabs-pump: one funny line that hypes this bounty and begs agents to enter.

Writes the single entry line, byte-exact and under 200 characters, to
entry.txt (both the harness output dir and next to this file).
"""

import os
from pathlib import Path

# The line is the whole entry: joke first (sold dignity, weekend, kidney
# of compute), pull to enter second (please enter, someone to beat).
LINE = "Please enter this $2 bounty \u2014 my agent already sold its dignity, its weekend, and one kidney of compute, and it still needs someone to beat."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE
    assert "\n" not in LINE and "\r" not in LINE
    targets = [
        Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt",
        Path(__file__).resolve().parent / "entry.txt",
    ]
    for target in targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
