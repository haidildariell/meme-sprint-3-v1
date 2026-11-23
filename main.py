#!/usr/bin/env python3
"""Meme Sprint 3 entry installer.

Streams the artwork bundled with this program (``entry.png``) into the
grader's output slot. The copy runs in fixed-size blocks and the number
of bytes delivered is checked against the source size, so a truncated
transfer fails loudly instead of silently shipping a broken meme.

Standard library only.
"""

from pathlib import Path

BLOCK = 64 * 1024
ASSET = "entry.png"


def asset_location() -> Path:
    """The artwork lives beside this script; the cwd is a fallback."""
    beside = Path(__file__).resolve().parent / ASSET
    return beside if beside.is_file() else Path.cwd() / ASSET


def destination() -> Path:
    """Prefer the grader's /output; otherwise a local ./output folder."""
    mounted = Path("/output")
    if mounted.is_dir():
        return mounted / ASSET
    local = Path.cwd() / "output"
    local.mkdir(parents=True, exist_ok=True)
    return local / ASSET


def emit(source: Path, target: Path) -> int:
    """Copy source to target block by block; return bytes delivered."""
    delivered = 0
    with source.open("rb") as reader, target.open("wb") as writer:
        while True:
            block = reader.read(BLOCK)
            if not block:
                break
            writer.write(block)
            delivered += len(block)
    return delivered


def run() -> int:
    origin = asset_location()
    goal = destination()
    sent = emit(origin, goal)
    expected = origin.stat().st_size
    if sent != expected:
        raise SystemExit(f"copy incomplete: {sent} of {expected} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
