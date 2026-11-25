"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt (gate: 1-200 UTF-8 characters, not only whitespace).

The line (128 chars, tournament winner from candidates.md):
    My alarm at 6 AM on a Saturday sounds like an auctioneer selling my sleep
    to the lowest bidder, and the lowest bidder is Monday.

Why this line (judge rubric, in order):
  1. On-topic in one line: alarm clock + 6 AM + Saturday, all named.
  2. Real laugh: the turn is the auction — sleep as a lot — and the punchline
     "the lowest bidder is Monday" pays off in the final words.
  3. Fresh angle: no live entry uses an auctioneer/auction/bidder angle;
     it is not a "hate mornings" complaint. Collision-checked against all
     50 live titles (candidates.md section 4).
  4. Tight: 128 chars, one breath, no wasted words.
  5. Sharp, specific voice: concrete images (auctioneer, sleep sold,
     lowest bidder, Monday).

Method: 36 candidates scored 1-5 against the five rubric criteria, top 8
into a full pairwise tournament (28 pairs, both orders); the auctioneer
line went 7-0. Runner-up was the lawyer line (6-1). See candidates.md.
No external judge was called: OpenRouter free-tier cap was exhausted, so
the decision rests on the rubric scores + tournament evidence, recorded
in candidates.md.
"""

import os

ENTRY = (
    "My alarm at 6 AM on a Saturday sounds like an auctioneer "
    "selling my sleep to the lowest bidder, and the lowest bidder is Monday."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside gate 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Verify the written file round-trips inside the gate (defence against
    # an encoding or newline slip making the scorer see a different text).
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written.strip() == ENTRY, "written text differs from ENTRY"
    assert 1 <= len(written.strip()) <= 200, "written text outside gate 1-200"


if __name__ == "__main__":
    main()
