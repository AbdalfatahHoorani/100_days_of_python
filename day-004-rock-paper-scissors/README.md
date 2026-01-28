# Day 4: Rock Paper Scissors 🪨📄✂️

This is the fourth project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a command-line version of the classic game Rock, Paper, Scissors, featuring a randomized computer opponent and ASCII art visuals.

## 📝 Description
The program allows a user to play Rock, Paper, Scissors against the computer. The user inputs a number representing their choice, and the computer generates a random choice. The program then displays the corresponding ASCII art for both choices and declares a winner, loser, or a draw based on the game's rules.

## ✨ Features
- **Randomization:** Uses the `random` module to generate the computer's move.
- **ASCII Art Visuals:** Displays hand symbols for Rock, Paper, and Scissors to make the game interactive.
- **Game Logic:** Uses conditional statements to compare the user's input against the computer's choice to determine the outcome.
- **Modular Design:** Utilizes a separate file (`choices.py`) to store and manage the list of hand symbols.

## 💡 What I Learned
- **Importing Modules:** Using the built-in `random` library to create unpredictable behavior.
- **Working with Lists:** Storing and retrieving data (ASCII art) from a list using indices.
- **Conditional Logic:** Building complex `if/elif` structures to handle all possible game outcomes.
- **Project Organization:** Importing variables and data from another local Python file.
- **Index Management:** Using user input to grab specific items from a list.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Make sure both `RockPaperScissors.py` and `choices.py` are in the same folder.
3. Save the code files.
4. Run the script using your terminal or IDE:
   ```bash
   python RockPaperScissors.py