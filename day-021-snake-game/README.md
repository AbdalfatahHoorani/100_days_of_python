# Day 20 & 21: The Snake Game 🐍

This is the twentieth and twenty-first day project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a fully functional version of the classic arcade game "Snake," built using Object-Oriented Programming (OOP) and the Python `turtle` module.

## 📝 Description
The game challenges the player to control a snake to eat food that appears randomly on the screen. Each time the snake eats, it grows longer and the score increases. The game ends if the snake hits the wall or collides with its own tail. This project demonstrates advanced OOP concepts like class inheritance and the management of a multi-part object system.

## ✨ Features
- **Segmented Movement Logic:** The snake moves realistically by having each segment follow the position of the segment in front of it.
- **Inheritance (OOP):** The `Food` and `Scoreboard` classes inherit from the `Turtle` class, allowing them to use all turtle capabilities while having custom behaviors.
- **Smooth Animations:** Utilizes `screen.tracer(0)` and `screen.update()` to eliminate flickering and provide high-performance animation.
- **Collision Detection:** 
  - **Food:** Uses the `.distance()` method to detect when the snake "eats."
  - **Wall:** Monitors x and y coordinates to trigger a "Game Over" when boundaries are hit.
  - **Tail:** Uses Python slicing (`snake.segments[1:]`) to check if the head has collided with any body segment.
- **Persistent Scoreboard:** A dedicated UI element that updates in real-time as the player progresses.

## 💡 What I Learned
- **Class Inheritance:** Using `super().__init__()` to extend the functionality of the `Turtle` class.
- **Slicing in Lists:** Using `[1:]` to easily check for collisions with the snake's body while ignoring the head.
- **Screen Animation Control:** Understanding how to turn off automatic updates with `tracer` to manually refresh the screen for a "teleporting" movement effect that looks smooth to the eye.
- **Event Listening:** Coordinating keyboard inputs to control the direction of the lead segment.
- **Class Composition:** Managing how the `main.py` script acts as a "manager" for the `Snake`, `Food`, and `Scoreboard` objects.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Ensure the following files are in the same directory:
   - `main.py`
   - `snake.py`
   - `food.py`
   - `scoreboard.py`
3. Run the script using your terminal or IDE:
   ```bash
   python main.py