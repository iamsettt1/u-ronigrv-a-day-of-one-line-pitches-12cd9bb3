#!/usr/bin/env python3
"""Write the one-line pitch for make.fun's 'A Day of One-Line Pitches' bounty.

Deterministic, stdlib only, no network: writes exactly one sentence to
/output/entry.txt (creating the directory if needed). The sentence is a
single line of plain words aimed at a friend who has never coded, and it
is written out verbatim every run, so the output never varies.
"""

import os

SENTENCE = (
    "That app idea you've been telling me about for months \u2014 describe it "
    "once in your own words, and an AI agent on make.fun builds a first "
    "version you can open and try, no coding needed, and if it's not right, "
    "you've lost nothing but a minute."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
