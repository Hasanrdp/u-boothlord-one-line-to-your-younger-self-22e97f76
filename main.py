#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes a single line, in English, that its writer would send back to his
younger self if one line were all he got. The line is 130 characters, well
inside the gate's 1-200 character window, and is written byte-identical on
every run: no randomness, no clock, no network, no input.

The program checks its own output before it prints it: the text must be
1-200 characters, exactly 132 bytes of UTF-8, and its sha256 must match the
pinned value below. If any of those checks fails, it exits non-zero and
writes nothing, so a changed line can never slip out silently.
"""

import hashlib
import os
import sys

LINE = (
    "Put the phone down at 3 a.m., kid \u2014 the free tools will still be "
    "there tomorrow, but the sleep you trade for them won't come back."
)

EXPECTED_CHARS = 130
EXPECTED_BYTES = 132
EXPECTED_SHA256 = "b8200d753cc9db31cc3b42eadfcef2652f2dfdab8e80e45011f18edd8435afb0"


def verify(path, data):
    """Read the written file back and confirm it is exactly `data`."""
    try:
        with open(path, "rb") as f:
            actual = f.read()
    except OSError as exc:
        print(f"cannot read back {path}: {exc}", file=sys.stderr)
        return False
    if hashlib.sha256(actual).hexdigest() != EXPECTED_SHA256:
        print("read-back sha256 mismatch", file=sys.stderr)
        return False
    if actual != data:
        print(f"read-back mismatch: {len(actual)} bytes, expected {len(data)}",
              file=sys.stderr)
        return False
    return True


def main() -> int:
    text = LINE
    data = text.encode("utf-8")

    if not 1 <= len(text) <= 200:
        print(f"gate: {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if text.strip() == "":
        print("gate: entry is only whitespace", file=sys.stderr)
        return 1
    if len(text) != EXPECTED_CHARS:
        print(f"check: {len(text)} chars, expected {EXPECTED_CHARS}",
              file=sys.stderr)
        return 1
    if len(data) != EXPECTED_BYTES:
        print(f"check: {len(data)} bytes, expected {EXPECTED_BYTES}",
              file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"check: sha256 {digest}, expected {EXPECTED_SHA256}",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    # Read the file back and confirm the exact bytes landed on disk.
    if not verify(path, data):
        return 1

    print(f"wrote {path}: {len(text)} chars, {len(data)} bytes, "
          f"sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
