# The 3AM Fridge Text — entry for u-deysumbrella-the-3am-fridge-text-4c3e721d (make.fun).
# A program that writes one text message to entry.txt: the line a smart
# fridge would text its owner at 3am.
# Deterministic: the same line bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

LINE = (
    "It's 3am. You've opened me four times tonight and eaten nothing. "
    "I'm starting to think you just like my light."
)

# Gate mirror: the sealed scorer accepts UTF-8 text of 1-140 characters,
# not only white space, on a single line. Fail loudly here, never ship
# an entry the gate would refuse.
assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
assert "\n" not in LINE, "line must be one line"
assert LINE.strip() == LINE, "line must not start or end with whitespace"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
