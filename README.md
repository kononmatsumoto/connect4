# Connect Four (Pygame Edition)

This is a desktop version of the classic Connect Four game implemented in Python using the Pygame library. The game allows two players to take turns dropping pieces into a 7x6 grid. The first player to align four of their pieces in a row—horizontally, vertically, or diagonally—wins the game.

## How to Play

- Run the game.
- Player 1 (red) and Player 2 (yellow) alternate turns.
- Click a column to drop your piece.
- First to 4 in a row wins!

## Project Structure

```
connect4pygame/
├── board.py        # Game logic (drop, check win, validate move)
├── constants.py    # Visual and dimensional constants
├── game.py         # Game loop and rendering logic
├── main.py         # Entry point that starts the game
```

## ▶️ Getting Started

### 1. Install Dependencies

Make sure Python and `pygame` are installed:

```bash
pip install pygame
```

### 2. Run the Game

```bash
python3 main.py
```

## Features

- Turn-based 2-player gameplay
- Color-coded tokens (red and yellow)
- Win detection in all directions
- Graphical interface using Pygame

## Next Improvements

- Add AI opponent
- Add restart/undo buttons
- Sound effects or animations

## Built With

- Python 3.8+
- [Pygame](https://www.pygame.org/)

## License

This project is for educational use. Feel free to modify or extend it.
