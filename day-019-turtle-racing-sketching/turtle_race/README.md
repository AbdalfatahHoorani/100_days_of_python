# Day 19: Turtle Racing Game 🐢🏎️

This is the nineteenth project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a graphical racing game where multiple turtle instances compete against each other, and the user tries to predict the winner.

## 📝 Description
The program uses the Python `turtle` module to create a racing track and six different colored turtles. At the start, the user is prompted to place a bet on which turtle they think will win. The turtles then move forward by random increments in a `while` loop. The game ends as soon as one turtle reaches the right edge of the screen, and the program announces whether the user won or lost their bet.

## ✨ Features
- **Interactive Betting:** Uses `screen.textinput()` to capture the user's choice before the race begins.
- **Multiple Instances:** Dynamically creates six unique `Turtle` objects, each with its own color and starting position.
- **Randomized Racing:** Uses the `random` module to generate a different "speed" (step distance) for each turtle in every iteration of the loop.
- **Coordinate Tracking:** Monitors the `xcor()` (x-coordinate) of every turtle to detect when one has crossed the finish line.
- **Automated Winner Logic:** Automatically compares the color of the winning turtle instance with the user's input string.

## 💡 What I Learned
- **Object Instances:** Creating multiple objects from the same class (`Turtle`) and managing them within a list.
- **Coordinate Systems:** Setting up a custom screen size with `setup()` and placing objects using specific x and y coordinates.
- **State Management:** Using a boolean flag (`game_on`) to control when the game loop should start and stop.
- **List Management:** Using a loop to iterate through a list of objects and perform actions (moving) on each one individually.
- **Input Handling:** Normalizing user input and comparing it against object attributes (like `pencolor`).

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. The `turtle` module is part of the Python Standard Library.
3. Save the code as `main.py`.
4. Run the script using your terminal or IDE:
   ```bash
   python main.py