#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one funny patch note for a bug in real life / human biology
to /output/entry.txt. Stdlib only, deterministic.
"""

import os

ENTRY = "v3.1.4: Fixed a bug where the brain replayed an embarrassing moment from 2009 at 3 a.m. for no reason."


def validate(text):
    """Mirror the bounty gate: 1-160 chars, UTF-8, not only whitespace."""
    text.encode("utf-8")
    if not 1 <= len(text) <= 160:
        raise ValueError("entry must be 1-160 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
