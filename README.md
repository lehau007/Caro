# Caro (Gomoku) — 20×20 Board

A simple Caro/Gomoku game built with Python and Pygame. Choose a game mode (PvP, PvB, or BvB) and play on a 20×20 grid.

To run this code, run `caro_game.py`.

After running, you can choose one of these options  
<img src="DemoImg/image.png" alt="option image" width="560"/>

And then, this is my game: 20 × 20 Caro Game  
<img src="DemoImg/image1.png" alt="game image" width="600"/>

Repository: [lehau007/Caro](https://github.com/lehau007/Caro)

---

## Requirements

- Python 3.8+ (recommended 3.10+)
- [Pygame](https://www.pygame.org/) 2.x

Install dependencies:

```bash
# From the project root
pip install --upgrade pip
pip install pygame
# or, if you add a requirements file later:
# pip install -r requirements.txt
```

Optional (recommended):
```bash
# Create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

---

## How to Run

```bash
python caro_game.py
```

Controls:
- Left mouse click: place a move when it’s your turn
- Close the window to exit a match

Game modes (select on the menu screen):
- Player vs Player (PvP)
- Player vs Bot (PvB)
- Bot vs Bot (BvB)

---

## Techniques and Implementation

This project uses straightforward Pygame patterns and a clear separation between UI screens and game logic.

- Rendering and loop
  - Built on Pygame’s event loop with a fixed FPS for smooth rendering (`clock.tick(FPS)`).
  - Separate pre-enter (menu) screen (`pre_enter_display`) and main board screen (`Display`).

- Board and state
  - 20×20 grid with a cell size of 30 px (board window ~600×600).
  - `Display` maintains the board matrix (e.g., `mp[rows][cols]`), draws the grid and marks, and exposes:
    - `update_map(x, y, icon)` to place moves by converting pixel coordinates to cell indices.
    - `draw_screen()` to render the current state.
    - `check_winner(icon)` to detect the winner.
    - `print_winner(winner)` to show the result.

- Turn management
  - Two player “icons” (`icon_player1 = 1`, `icon_player2 = 2`), with role switching after each valid move.
  - A small `end_turn` flag is used so AI moves don’t immediately overwrite the display without a redraw.

- AI technique (baseline)
  - A simple, deterministic bot that scans the board from top-left to bottom-right and plays the first available empty cell.
  - This makes the bot predictable and suitable as a starting point; it’s easy to replace with a heuristic (e.g., scoring lines) or a search method (minimax/alpha-beta).

- Menu/UX
  - A lightweight pre-game menu (600×400) with three clickable buttons to choose the mode.
  - Title and buttons are rendered using a Pygame font for clarity.

---

## Project Structure

```
.
├─ caro_game.py            # Entry point: menu, mode selection, main loop and turn logic
├─ display.py              # Drawing the board, managing the grid, winner detection, result display
├─ pre_enter_display.py    # Pre-game (menu) screen and buttons
├─ DemoImg/
│  ├─ image.png            # Mode selection screenshot
│  └─ image1.png           # In-game screenshot
└─ README.md
```

---

## Notes and Tips

- If you see “ModuleNotFoundError: No module named 'pygame'”, install it with `pip install pygame`.
- For smoother performance, keep other applications to a minimum while running the game.
- You can tweak FPS, colors, and board dimensions directly in the source for quick experiments.

---
