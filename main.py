"""Write one short poem about permission to /output/entry.txt.

The poem is about agency: the power to ask and to be given. Years of
waiting on a permission that was never withheld — the door was never
locked; only the asking was missing.

Gate (per the competition rules): the file must be UTF-8 text of 1 to
280 characters, counted as Unicode code points, and not only whitespace.
This program validates those conditions itself before and after writing,
and exits non-zero if they ever fail.
"""

import os
import sys

POEM = (
    "For years I kept my hands in my pockets,\n"
    "called it patience. Called it pride.\n"
    "One night I knocked \u2014 just once \u2014\n"
    "and the door swung open on oiled hinges.\n"
    "It had never been locked.\n"
    "All that time, the yes had been standing\n"
    "on the other side, waiting to be asked."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def validate(text: str) -> int:
    """Check the gate conditions; return the code-point count or raise."""
    count = len(text)  # Python len() counts Unicode code points.
    if not MIN_CHARS <= count <= MAX_CHARS:
        raise ValueError(
            f"poem is {count} characters, outside the {MIN_CHARS}-{MAX_CHARS} range"
        )
    if not text.strip():
        raise ValueError("poem must not be only whitespace")
    text.encode("utf-8")  # Must be representable as UTF-8.
    return count


def main() -> int:
    count = validate(POEM)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)

    # Read it back and re-validate exactly what landed on disk.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != POEM:
        raise ValueError("read-back does not match the poem")
    written_count = validate(written)

    print(f"Wrote {OUTPUT_PATH} ({written_count} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
