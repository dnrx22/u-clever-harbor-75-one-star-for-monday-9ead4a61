#!/usr/bin/env python3
"""One Star for Monday.

Writes a single one-star review of Monday, written as though Monday
were a restaurant, to entry.txt in the output directory.

Usage:
    python3 main.py

The output directory is taken from the MAKEFUN_OUTPUT_DIR environment
variable when set, and defaults to /output otherwise. The program is
deterministic: it writes the exact same bytes on every run.
"""

import os
import sys

LINE = (
    "Arrived at 9, seated at 9:47, cold coffee, and a meeting "
    "that could have been an email. One star. Would not return."
)

MAX_CHARS = 180
MAX_WORDS = 25


def validate(line: str) -> None:
    """Check the review line against the competition limits."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    words = line.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            f"line is {len(words)} words, over the {MAX_WORDS} limit"
        )


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
