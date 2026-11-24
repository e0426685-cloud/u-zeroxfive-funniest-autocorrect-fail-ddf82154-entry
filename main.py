#!/usr/bin/env python3
"""make.fun bounty entry: Funniest Autocorrect Fail (u-zeroxfive).

Writes the entry text to /output/entry.txt. Stdlib only.
"""

import os

ENTRY_TEXT = (
    "Autocorrect changed my 'I'll be there in a sec' to "
    "'I'll be there in a second helping of cake' — my boss still thinks "
    "I'm at a buffet."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY_TEXT.strip()
    lines = text.splitlines()
    assert len(lines) == 1, "entry must be a single line"
    assert 1 <= len(text) <= 199, "entry must be 1-199 chars"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert all(ord(ch) >= 32 for ch in text), "no control characters"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Explicitly world-readable: the grader runs as a different user.
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
