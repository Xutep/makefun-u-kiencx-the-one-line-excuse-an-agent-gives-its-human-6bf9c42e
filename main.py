#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

The excuse is a single line, under 160 characters: the excuse an AI
agent gives its human for missing a deadline. It is written out
deterministically, with no input, no network and no randomness, so
every run produces byte-identical output.
"""

import os

EXCUSE = (
    "I stored your deadline in my context window, "
    "then evicted it to make room for this apology."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
