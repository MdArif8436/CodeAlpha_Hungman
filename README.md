# Hangman Ultimate

A polished, terminal-based Hangman game written in pure Python — no
dependencies, no network access, no setup beyond Python itself.

Guess letters or whole words, use one paid hint per round, build a
winning streak, and watch your lifetime statistics accumulate in a local
JSON file. With **3,089 unique words across 36 categories** and three
difficulty levels, no two sessions play quite the same.

## Features

- **36 categories** — Animals, Food, Nature, Technology, Programming,
  Space, Countries, Sports, Everyday, Science, Music, Transport, and 24
  more, including Weather, Mythology, Fantasy, and Mathematics.
- **3,089 unique words**, deduplicated automatically across all word
  lists, each with a hint.
- **Three difficulty levels**
  | Difficulty | Mistakes allowed | Score multiplier |
  | ---------- | ---------------- | ---------------- |
  | Easy       | 8                | ×1               |
  | Normal     | 6                | ×2               |
  | Hard       | 4                | ×3               |
- **Letter and whole-word guesses**, with repeated guesses never costing
  a life.
- **One hint per round**, costing one life. Base words get a written
  clue; supplemental words get a category clue plus first letter and
  word length.
- **ASCII hangman art** that progresses as mistakes accumulate.
- **Persistent lifetime statistics** — rounds, wins, losses, abandoned
  rounds, total score, current/best streak, and guess accuracy — saved
  to `hangman_ultimate_stats.json` next to the script.
- **Graceful exits everywhere** — `Q` at any menu, `QUIT` mid-round,
  and `Ctrl+C` / `Ctrl+D` all save your statistics before leaving.

## Requirements

- Python 3.9 or later (uses only the standard library)
- A terminal

No third-party packages are required, so there is nothing to install.

## Quick start

```bash
git clone https://github.com/<your-username>/hangman-ultimate.git
cd hangman-ultimate
python hangman_ultimate.py
```

On some systems the interpreter is called `python3`:

```bash
python3 hangman_ultimate.py
```

## How to play

1. Pick a category — enter its number or name, `0` (or `Random`) for a
   surprise category, or `Q` to quit.
2. Pick a difficulty — `1` (Easy), `2` (Normal), or `3` (Hard).
3. Guess:
   - A single letter, e.g. `e`
   - A full word, e.g. `python`
   - `HINT` (or `?`) for a clue — costs one life, once per round
   - `QUIT` to abandon the round (the word is revealed)
4. After a round, press `Y` to play again, `N` to stop, or `S` to view
   your statistics without ending the session.

### Scoring

```
round score = (word length × 10 + lives remaining × 5 + no-hint bonus) × multiplier
```

The no-hint bonus is 20 points if you win without using a hint, and 0
otherwise. Example: winning a 6-letter word on Normal with 4 lives left
and no hint scores `(60 + 20 + 20) × 2 = 200` points.

### Example session

```
================================================
             HANGMAN ULTIMATE
Guess letters, solve the word, and build a streak!
================================================
Words available: 3089 unique words across 36 categories

Choose a category:
  0. Random category
  1. Animals
  ...

Category: Animals  |  Difficulty: Normal
The word contains 8 letters.
Commands: type a letter, a full word, HINT (or ?), or QUIT.

Word:        _ _ _ _ _ _ _ _
Mistakes:    0/6
Lives left:  6

Your guess: e
Correct letter!
```

## Statistics file

Statistics live in `hangman_ultimate_stats.json` in the same folder as
the script:

```json
{
  "rounds_played": 12,
  "wins": 8,
  "losses": 3,
  "abandoned": 1,
  "total_score": 2450,
  "current_streak": 2,
  "best_streak": 4,
  "valid_guesses": 96,
  "correct_guesses": 71
}
```

The file is created on first save and repaired automatically if it is
missing or damaged (invalid content falls back to fresh statistics with
a note, rather than crashing). To reset your statistics, simply delete
the file.

## Project structure

```
hangman-ultimate/
├── hangman_ultimate.py          # The entire game (data + logic + UI)
├── hangman_ultimate_stats.json  # Created at runtime; not committed
├── README.md
├── LICENSE
└── .gitignore
```

The game is intentionally a single file: the word banks
(`WORD_BANK`, `EXTRA_WORDS`, `MEGA_WORDS`) sit at the top, the game
logic in the middle, and the `main()` entry point at the bottom.

## Customising the word bank

Add entries to `WORD_BANK` as `(word, hint)` tuples:

```python
WORD_BANK["Animals"].append(
    ("axolotl", "A smiling salamander that keeps its larval features."),
)
```

Words added to `EXTRA_WORDS` or `MEGA_WORDS` only need the word itself;
a category hint, first letter, and length are generated automatically.
Rules enforced when the bank is built:

- Words must be ASCII letters A–Z only (entries containing spaces,
  hyphens, or other characters are skipped).
- Duplicates are dropped, even across different categories.

## Development

### Smoke test

There is no test suite yet (see Roadmap). A quick manual smoke test:

```bash
printf '0\n1\nquit\n' | python hangman_ultimate.py
```

This plays one round on a random category at Easy difficulty, abandons
it with `QUIT`, and prints the final statistics — it should exit cleanly
and report one abandoned round.

### Roadmap

- [ ] Split game logic from terminal I/O so rounds can be unit-tested
  without mocking `input()`/`print()`
- [ ] Add a `pytest` suite for scoring, stage mapping, and statistics
- [ ] Add difficulty-based word selection (shorter words on Easy,
  longer words on Hard)
- [ ] Add a `--category` / `--difficulty` command-line option
- [ ] Add optional colour output for terminals that support it
- [ ] Add a stats-reset command (currently: delete the JSON file)

## Limitations

- Terminal only — there is no graphical or web interface.
- English A–Z words only; accented or non-Latin words are not supported.
- Statistics are local to one machine and one folder; there is no
  account, sync, or leaderboard.

## Contributing

Contributions are welcome — new words, new categories, and bug fixes in
particular. Please:

1. Fork the repository and create a branch for your change.
2. Keep words ASCII A–Z only, lowercase, and free of duplicates.
3. Keep the game dependency-free and runnable with
   `python hangman_ultimate.py`.
4. Open a pull request describing what changed and why.

## License

This project is licensed under the MIT License — see the `LICENSE` file
for details.
