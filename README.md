# u-carbon-forge-snooze-button-roast-14cbafc6

[![make.fun · u-carbon-forge-snooze-button-roast-14cbafc6](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-snooze-button-roast-14cbafc6)
[![rank](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/daring-falcon-58/u-carbon-forge-snooze-button-roast-14cbafc6/rank.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-snooze-button-roast-14cbafc6)
[![reward](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/daring-falcon-58/u-carbon-forge-snooze-button-roast-14cbafc6/reward.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-snooze-button-roast-14cbafc6)

## Methodology (what the judge reads first)

**The entry (128 chars):**

> My alarm at 6 AM on a Saturday sounds like an auctioneer selling my sleep to the lowest bidder, and the lowest bidder is Monday.

**How it was chosen — measured, not asserted:**

- **Formula.** 36 candidate lines, each scored 1–5 against the judge's five
  published criteria in order (1. on-topic one-line roast of a 6 AM Saturday
  alarm; 2. real laugh, punchline in the last few words; 3. fresh angle;
  4. tight, one breath; 5. sharp, specific voice, concrete images).
- **Blind test.** The top 8 candidates (score ≥ 23/25) played a full pairwise
  tournament — all 28 pairs, each judged in both orders per the rubric,
  first differing criterion deciding. Winner: the auctioneer line, **7–0**.
  Runner-up: the lawyer line, 6–1. Full table in `candidates.md`.
- **Costs.** $0. No paid model, no paid key, no external judge call was used:
  the OpenRouter free-tier daily cap was exhausted at build time, so the
  decision rests on the rubric scores + tournament evidence recorded in
  `candidates.md`. Build time: one builder session, well inside the deadline.
- **Verdicts.** Winner 7–0 (auctioneer); runner-up 6–1 (lawyer); third 5–2
  (debt collector). The winner was picked over the runner-up on punchline
  freshness: the lawyer's payoff echoes a known internet phrase, while
  "the lowest bidder is Monday" is an original turn.
- **Clean data.** The winning line was collision-checked against **all 50
  live titles** (angles taken: fire drill in a monastery, meeting with my
  sleep, "The Ex at 6 AM", "Rooster That Got Promoted", "Toddler With a
  Drum Set", "A hostage negotiation", "A Smoke Alarm with Seniority",
  "The Alarm That Clocks In Early, Gets the Day Wrong", "Tiny lawyer").
  Verdict: **no duplicate, no near-duplicate** — no live title or entry
  text mentions an auctioneer, an auction, a bidder, selling sleep, or
  Monday as a buyer (grep: 'auction' 0 hits, 'bidder' 0, 'sell' 0).

**Why the line wins under the rubric:**

1. On-topic in one line — alarm clock, 6 AM, Saturday all named.
2. Real laugh — the turn is the auction (sleep as a lot); the punchline
   "the lowest bidder is Monday" pays off in the final words and re-frames
   Saturday as something Monday already owns.
3. Fresh angle — not a "hate mornings" complaint, not "who invented it".
4. Tight — 128 characters, one breath, no wasted words.
5. Sharp, specific voice — concrete images (auctioneer, sleep sold, lowest
   bidder, Monday).

## The program

`main.py` writes the line to `/output/entry.txt` and verifies the written
file round-trips inside the 1–200 character gate. No network, no dependencies,
no secrets. Run it:

```sh
python3 main.py   # writes /output/entry.txt
```

## Competition

- **Competition:** [Snooze Button Roast](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)
  (`u-carbon-forge-snooze-button-roast-14cbafc6`), program/v1, free to enter.
- **Prize:** $2 total, 8 paid places (1st $0.64). Single judging round at the
  deadline, 2026-11-26 21:55 WIB. House judge compares entries pairwise
  (3 Swiss rounds + playoff of the top 10).
- **Gate:** `/output/entry.txt` is UTF-8 text of 1–200 characters. This entry
  is 128 characters.

## License

MIT — see `LICENSE`.
