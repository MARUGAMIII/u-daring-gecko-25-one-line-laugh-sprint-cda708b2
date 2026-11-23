#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes a single original funny line (at most 200 characters) about
everyday life to /output/entry.txt.
"""

import os

LINE = "I asked my smart speaker for something relaxing, so it read my unread emails out loud in a soothing voice."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
