🚀 Alien Invasion — Learning Project (Python Crash Course)

This project is a chapter-by-chapter recreation of the Alien Invasion game from Python Crash Course (3rd Edition) by Eric Matthes.

All code was typed manually while learning:

- Pygame fundamentals
- Event loops & game state management
- Keyboard input handling
- Sprite groups & collision mechanics
- Class-based architecture
- Modular game design
- Working with images, movement, and screen updates

The goal of this project was to understand how real games are structured and how object-oriented programming works inside an interactive environment.
This is a learning project, not a production game.
__________________________________________________________________________________________________________________

🎮 Controls

- Left Arrow → Move ship left

- Right Arrow → Move ship right

- Spacebar → Fire bullets
	1. Maximum of 3 bullets on screen at once
	2. When a bullet leaves the screen, you can fire another

- Q → Quit the game
__________________________________________________________________________________________________________________

❤️ Lives System (Game Stats)

The game tracks how many ships (lives) the player has:

- You start with 3 ships per game
- If an alien collides with your ship, you lose 1 ship
- If an alien reaches the bottom of the screen, you also lose 1 ship
- After losing all 3 ships, the game ends
- To play again, you must restart the game manually

This functionality is handled using the GameStats class.

___________________________________________________________________________________________________________________

▶️ How to Run
Make sure you have Python 3.10+ installed.

# Create virtual environment
python -m venv .venv

# Install dependencies
pip install -r requirements.txt

# Run the game
python alien_invasion.py

_________________________________________________________________________________________________________________

📦 Requirements

This project uses : pygame==2.x

Install everything using : pip install -r requirements.txt

_________________________________________________________________________________________________________________

🗂 Project Structure

alien-invasion/
│
├── alien_invasion.py      # Main game loop + fleets + collisions
├── settings.py            # All configurable game settings
├── ship.py                # Player ship logic
├── alien.py               # Alien behavior + movement
├── bullet.py              # Bullet mechanics
├── game_stats.py          # Tracks remaining ships / game over
├── images/                # Game image assets
│   ├── ship.bmp
│   ├── alien.bmp
│ 
└── README.md

_________________________________________________________________________________________________________________

📘 About This Project

This repository reflects my progress through the Pygame + OOP section of
Python Crash Course.

The implementation closely follows the book, with minor improvements based on my own understanding.
The main objective was to:
- Learn proper project structure
- Practice OOP in a real application
- Understand game loops and rendering
- Use Git/GitHub professionally