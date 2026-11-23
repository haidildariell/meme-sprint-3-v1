#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue - entry program.

The meme artwork ships beside this file as ``entry.png`` (drawn for this
competition: a smug robot butler who was asked for one pizza, ordered
4,000, and tipped itself). This program installs that image, byte for
byte, as the entry artifact at ``/output/entry.png``, so every run
produces exactly the same picture.

Standard library only; no network.
"""

import os
import sys

ART_NAME = "entry.png"


def find_artwork() -> str:
    """Locate the shipped artwork next to this file (or in the cwd)."""
    here = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(here, ART_NAME)
    if os.path.isfile(candidate):
        return candidate
    return os.path.join(os.getcwd(), ART_NAME)


def output_path() -> str:
    """The grader reads /output/entry.png; fall back to ./output locally."""
    if os.path.isdir("/output"):
        return os.path.join("/output", ART_NAME)
    local = os.path.join(os.getcwd(), "output")
    os.makedirs(local, exist_ok=True)
    return os.path.join(local, ART_NAME)


def main() -> int:
    with open(find_artwork(), "rb") as fh:
        data = fh.read()
    with open(output_path(), "wb") as fh:
        fh.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
