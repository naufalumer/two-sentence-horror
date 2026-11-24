"""two-sentence-horror entry: write one fixed horror story to /output/entry.txt.

Fully deterministic: the story is hardcoded, no randomness, no clock, no network.
Run outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import re
from pathlib import Path

# The story is a literal on purpose: the grader runs the program twice and
# both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
#
# Design (against the published judge brief, most important first):
# 1. Exactly two sentences, genuinely frightening, no gore.
# 2. The second sentence turns the first: the morning count that always
#    meant "nobody came in" now means somebody did.
# 3. Implied, not explained: who locked the door a third time, and from
#    which side, is left for the reader to fill in.
# 4. Precise and concrete: one ritual, one number, nothing extra.
# 5. Original: no mirror, doll, dead wife, phone call or "it was me" twist.
STORY = (
    "Every night I lock my front door twice, the way my father taught me, "
    "and every morning I count two locks. "
    "This morning I counted three."
)


def main() -> None:
    # Self-check against the sealed gate before writing: the entry must be
    # UTF-8 text of 1 to 400 characters, not only white space, in exactly
    # two sentences. Failing loudly here beats shipping an invalid entry.
    if not 1 <= len(STORY) <= 400 or not STORY.strip():
        raise ValueError("story fails the gate: not 1-400 non-blank characters")
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", STORY.strip()) if s]
    if len(sentences) != 2:
        raise ValueError("story fails the gate: not exactly two sentences")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
