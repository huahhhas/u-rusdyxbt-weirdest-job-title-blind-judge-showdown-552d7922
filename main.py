#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown entry.

Writes one original job title, and nothing else, to /output/entry.txt.
Pure Python standard library, no dependencies, fully deterministic.
"""

import os

TITLE = "Chief Apologizer for Elevators Stuck Between Floors"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
