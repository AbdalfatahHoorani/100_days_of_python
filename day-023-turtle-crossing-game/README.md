# Day 23: Turtle Crossing Game 🐢🚗

This is the twenty-third project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a "Frogger-style" arcade game where the player controls a turtle attempting to cross a busy road filled with moving cars without getting hit.

## 📝 Description
The goal of the game is to move the turtle from the bottom of the screen to the top. As the turtle moves, cars of different colors are generated at random intervals on the right side of the screen and move toward the left. If the turtle reaches the top, it resets to the starting position (representing a level completion). If the turtle collides with a car, the game ends.

## ✨ Features
- **Player Movement:** Simple vertical movement controls using the "Up" and "Down" arrow keys.
- **Dynamic Car Spawning:** A `CarManager` class that generates car objects at random Y-coordinates and manages their movement across the screen.
- **Collision Detection:** Uses the mathematical `distance()` method to calculate the proximity between the player and any car in the "garage" list.
- **Traffic Management:** Implements a spawning frequency logic (a car is created every 6th iteration of the game loop) to ensure the road isn't impassable.
- **Modular OOP Design:** Organized into separate files for the Player, Car Manager, and Scoreboard to keep the logic clean and scalable.

## 💡 What I Learned
- **Object Lists:** Managing a dynamic list of objects (the `garage`) where items are created and moved simultaneously.
- **Hitbox Logic:** Using the `.distance()` method to detect collisions between two graphical objects.
- **Game Loop Timing:** Using `time.sleep()` and a counter variable (`car_generator`) to control the pace of the game and the frequency of obstacles.
- **Screen Updates:** Using `screen.tracer(0)` to turn off automatic animations, allowing for a smoother "frame-by-frame" update style.
- **Coordinate Systems:** Mapping random integer ranges to the screen height to simulate different "lanes" of traffic.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Ensure all files (`main.py`, `player.py`, `car_manager.py`, and `scoreboard.py`) are in the same directory.
3. Run the game via the terminal:
   ```bash
   python main.py