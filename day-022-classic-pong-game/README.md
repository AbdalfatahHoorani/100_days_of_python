# Day 22: Classic Pong Game 🎾

This is the twenty-second project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a fully functional, two-player version of the classic arcade game Pong, built using Python's `turtle` graphics library and Object-Oriented Programming (OOP) principles.

## 📝 Description
The program creates a digital table tennis game where two players control paddles on opposite sides of the screen. The objective is to bounce a ball back and forth; if a player misses the ball, the opponent scores a point. The game features real-time collision detection, dynamic ball physics, and a live scoreboard.

## ✨ Features
- **Two-Player Gameplay:** Player 1 uses the "Up" and "Down" keys, while Player 2 uses the "W" and "S" keys.
- **Advanced Ball Physics:** Uses the `math` library to calculate ball trajectories using sine and cosine for smoother, randomized movement angles.
- **Collision Detection:** Logic for bouncing off top/bottom walls and interacting with the player-controlled paddles.
- **Dynamic Scoring System:** A central scoreboard that updates in real-time and detects when a player reaches the winning score (set to 3).
- **Smooth Animation:** Utilizes `screen.tracer(0)` and `screen.update()` for high-performance graphics without flickering.
- **Difficulty Scaling:** The ball slightly changes behavior and resets its position after every point scored.

## 💡 What I Learned
- **Inheritance in OOP:** Creating subclasses of the `Turtle` class (Paddle, Ball, Scoreboard) and using `super().__init__()` to extend functionality.
- **Coordinate Geometry:** Managing X and Y coordinates to handle movement, screen boundaries, and hitboxes.
- **Event Listeners:** Using `screen.listen()` and `onkeypress()` to map keyboard inputs to specific object methods.
- **Game Loops:** Implementing a `while` loop to manage the state of the game, including frame updates and logic checks.
- **Vector Mathematics:** Using `math.radians`, `math.cos`, and `math.sin` to handle ball speed and direction vectors.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Ensure all files (`main.py`, `paddle.py`, `ball.py`, and `scoreboard.py`) are in the same directory.
3. Run the game via the terminal:
   ```bash
   python main.py