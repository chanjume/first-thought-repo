#!/usr/bin/env python3
"""Write one word to /output/entry.txt.

The word: vellichor -- the strange wistfulness of used bookstores,
which are infused with the past. The smell of old paper, dust, and
books that passed through other hands. Surprising, vivid, and
specific: one word that opens a whole room the moment you hear it --
a first thought, not a dictionary answer.
"""
import os

WORD = "vellichor"


def main():
    assert 1 <= len(WORD) <= 24, f"word must be 1-24 characters, got {len(WORD)}"
    assert WORD.strip() == WORD, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
