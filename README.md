🚀 Alien Invasion — Learning Project (Python Crash Course)

This repository contains a chapter-by-chapter implementation of the Alien Invasion game from  
Python Crash Course (3rd Edition)** by *Eric Matthes*, built using Python and Pygame.

All code was typed manually as part of learning and understanding how real games are structured using
object-oriented programming and event-driven design.

> ⚠️ This is a learning project, not a production-ready game.

_________________________________________________________________________________________________________________

📚 What I Learned

Through this project, I practiced and understood:

- Pygame fundamentals
- Event loops and frame-based updates
- Keyboard and mouse input handling
- Game state management (active / inactive / pause)
- Sprite groups and collision detection
- Class-based architecture (OOP)
- Modular project structure
- Rendering images and handling movement
- Difficulty scaling and score management

___________________________________________________________________________________________________________________

🎮 Gameplay Features

Core Mechanics
- Player-controlled ship with smooth movement
- Bullet firing system with collision detection
- Alien fleet generation with classic side-to-side movement
- Fleet direction change at screen edges
- Fleet drops downward when edges are hit

Game Systems
- Lives system
  - Player starts with 3 ships
  - Lose a ship if:
    1. An alien collides with the ship
    2. An alien reaches the bottom of the screen
- Scoring system
  - Score increases when aliens are destroyed
  - Scores are rounded for clean display
  - High score is tracked and shown at the top-center
- Level system
  - New level starts when the fleet is destroyed
  - Ship, bullets, and aliens move faster each level

UI & Game State
- Game starts in an inactive state
- Click the "Play" button to start
- Cursor hides during gameplay and reappears after game ends

_____________________________________________________________________________________________________________________

## 🎮 Controls

| Action           |     Key / Input         |
|------------------|-------------------------|
| Move Left        |     ← Left Arrow        |
| Move Right       |     → Right Arrow       |
| Fire Bullet      |       Spacebar          |
| Pause / Resume   |          `P`            |
| Start Game       |  Mouse Click on [Play]  |
| Quit Game        |          `Q`            |

> Maximum of 3 bullets can exist on screen at once.

_______________________________________________________________________________________________________________________

❤️ Lives System (GameStats)

- Player starts with 3 extra ships
- Ship count decreases when:
  - Alien collides with the ship
  - Alien reaches the bottom of the screen
- Game ends when ships reach zero
- Player can start a new game using the Play button

This logic is handled using the `GameStats` class.

_______________________________________________________________________________________________________________________________


🗂 Project Structure

alien-invasion/
│
├── alien_invasion.py      # Main game loop and event handling
├── settings.py            # All configurable game settings
├── ship.py                # Player ship logic
├── alien.py               # Alien behavior and movement
├── bullet.py              # Bullet mechanics
├── game_stats.py          # Tracks lives and game state
├── scoreboard.py          # Score, high score, and level display
├── button.py              # Play button UI
├── images/                # Game image assets
│   ├── ship.bmp
│   ├── alien.bmp
│
├── requirements.txt
└── README.md

___________________________________________________________________________________________________________________________________

▶️ How to Run

Requirements
- Python **3.10+**
- Pygame **2.x**

Setup & Run
```bash
# Create virtual environment
python -m venv .venv

# Activate environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python alien_invasion.py
