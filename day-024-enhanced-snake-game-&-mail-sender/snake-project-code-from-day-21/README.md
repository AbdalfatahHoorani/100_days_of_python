# Day 20-24: Snake Game with Persistent High Score

This is a refined version of the classic Snake Game. Unlike basic versions, this project implements a High Score system that saves your best score to a local file, ensuring it is remembered even after you close the program.

## 📝 Description
The player controls a snake that grows longer each time it eats food (blue circles). The game tracks the current score and compares it to a high score stored in `data.txt`. If the snake hits a wall or its own tail, the game resets, and the high score is updated if the player achieved a new record.

## ✨ Features
- **Persistent Data:** Uses `data.txt` to read and write the all-time high score using Python's File I/O.
- **Snake Growth:** Every time the snake eats food, a new segment is appended to the tail.
- **Collision Detection:** Sophisticated checks for wall boundaries and self-collision (tail-hitting logic).
- **Game Reset Logic:** Instead of a simple "Game Over," the snake resets to the center, and the score resets, allowing for continuous play.
- **Smooth Animation:** Uses the `tracer` and `update` methods for fluid movement.

## 💡 What I Learned
- **File I/O:** Using `with open() as file:` to read and write data to external text files.
- **Slicing and Lists:** Managing a list of turtle objects and using loops to move segments to the position of the previous segment.
- **State Management:** Tracking the `head` of the snake as a primary reference point for all collision logic.
- **Refactoring:** Organizing code into separate classes (`Snake`, `Food`, `Scoreboard`) for better maintainability.

## 🚀 How to Run
1. Ensure `main.py`, `snake.py`, `food.py`, `scoreboard.py`, and `data.txt` are in the same folder.
2. Run `main.py`:
   ```bash
   python main.py