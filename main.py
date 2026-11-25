"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes the GPS's own one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, no network, no input: every run writes the same line.
"""

import os

LINE = (
    "The map swore that dirt track was a shortcut, "
    "and the lake at the end agreed with me until your tires touched it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
