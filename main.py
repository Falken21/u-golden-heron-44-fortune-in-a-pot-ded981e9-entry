"""Fortune in a Pot - entry program.

Writes one kind, funny fortune for a houseplant to /output/entry.txt,
with no trailing newline. The fortune is a single line of at most 120
characters, as the competition gate requires.
"""

import os

ENTRY = (
    "You will outgrow your pot by spring, forgive the cat for the bite "
    "marks, and be watered on time twice in a row."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def entry_text() -> str:
    """Return the fortune, checked against the gate's limits."""
    assert 1 <= len(ENTRY) <= MAX_CHARS, "fortune must be 1-120 characters"
    assert "\n" not in ENTRY, "fortune must be a single line"
    return ENTRY


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry_text())


if __name__ == "__main__":
    main()
