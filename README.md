# Python Exercises

A collection of small Python projects built for learning and practice. Each project lives in its own file and focuses on a different topic or skill.

## About

This repository is not a single application — it is a **workspace for multiple Python exercises**. New projects are added over time as standalone scripts you can run independently.

## Projects

| Project     | File           | Description                                      |
|-------------|----------------|--------------------------------------------------|
| Blackjack   | `blackjack.py` | Terminal-based Blackjack game with ASCII cards   |

## Requirements

- Python 3.x

No external dependencies are required for the current projects.

## How to Run

From the project root, run any exercise directly:

```bash
python3 blackjack.py
```

## Project Structure

```
PythonExercises/
├── README.md
├── blackjack.py      # Blackjack game
└── ...               # Future exercises
```

## Blackjack

A command-line Blackjack game where you play against the dealer.

**Features:**
- ASCII card display with suit symbols (♠ ♥ ♦ ♣)
- Player turn: Hit or Stand
- Dealer follows standard rules (hits on 16, stands on 17)
- Win, lose, bust, and tie outcomes

**Gameplay:**
1. Two cards are dealt to the player and the dealer
2. Choose **H** to hit or **S** to stand on your turn
3. The dealer plays automatically after you stand
4. The hand closest to 21 without going over wins

---

More exercises will be added to this repository over time.
