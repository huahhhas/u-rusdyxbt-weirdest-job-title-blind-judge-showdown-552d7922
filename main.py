#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown entry.

Writes one original job title, and nothing else, to /output/entry.txt.
Pure Python standard library, no dependencies, fully deterministic.
"""

import os

# Title parts: role + what the role apologizes for. Built from parts so the
# title reads as one coherent job, not a pasted phrase.
# Twist: escalators don't just break — they quit, mid-ride, like a fed-up
# employee walking off the job. Funnier and more specific than a stuck lift.
_ROLE = "Senior Apologizer"
_SUBJECT = "Escalators That Quit Mid-Ride"

TITLE = f"{_ROLE} for {_SUBJECT}"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
