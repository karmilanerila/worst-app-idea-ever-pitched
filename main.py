#!/usr/bin/env python3
"""Blinkr — the world's first competitive blinking app.

Entry for the make.fun bounty "The Worst App Idea Ever Pitched"
(u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23).

The program writes a single sentence — one pitch for the worst, most
useless app imaginable — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

PITCH = (
    "Blinkr is the world's first competitive blinking app: it counts every "
    "blink, ranks you against your friends on a leaderboard, and pings you "
    "the moment a contact blinks faster, because your eyelids deserve a "
    "season and a trophy ceremony."
)


def main():
    # The bounty gate allows 1-240 characters; refuse to emit an invalid entry.
    assert 1 <= len(PITCH) <= 240, "pitch is {} chars".format(len(PITCH))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(PITCH.encode("utf-8"))
    os.chmod(path, 0o644)
    print("wrote {} ({} chars)".format(path, len(PITCH)))


if __name__ == "__main__":
    main()
