#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that
comes to mind, with no topic, no explanation and no second draft.
Standard library only; deterministic; no input, no network.
"""

import os

WORD = "vellichor"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 24 characters, not only
    # whitespace, and the task demands exactly one word: refuse to
    # write anything that is not a single alphabetic token.
    if not (1 <= len(WORD) <= 24):
        raise ValueError("word must be 1 to 24 characters")
    if not WORD.isalpha() or WORD != WORD.strip() or " " in WORD:
        raise ValueError("word must be exactly one alphabetic token")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
