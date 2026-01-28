# Day 7: Hangman Game 🎮

This is the seventh project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a classic text-based Hangman game where the player must guess a hidden word letter by letter before running out of lives.

## 📝 Description
The program selects a random word from a list, and the player attempts to reveal it by guessing letters. For every incorrect guess, the player loses a life, and the visual "Hangman" stage updates. The game includes logic to prevent the player from losing lives for repeating a letter they have already guessed.

## ✨ Features
- **Dynamic Word Display:** Shows the current progress of the word with underscores (e.g., `_ _ a _ _`).
- **Visual Feedback:** Uses a list of ASCII art stages to represent the "Hangman" as the player loses lives.
- **Redundancy Protection:** Tracks previously guessed letters in a list (`already_chosen`) and warns the user if they repeat a guess, preventing unnecessary life loss.
- **Win/Loss Conditions:** Automatically detects if the player has completed the word or if their lives have hit zero.
- **Case Sensitivity Handling:** Converts all user input to lowercase to ensure consistency with the game logic.

## 💡 What I Learned
- **Nested Loops and Logic:** Combining a `while` loop for the game state with `for` loops to check character positions.
- **List Manipulation:** Using indices to replace specific items in a list (replacing `_` with the correct letter).
- **State Management:** Tracking multiple variables like `lives`, `stage_level`, and `nice_choice` to control the flow of the game.
- **Membership Operators:** Using `in` and `not in` to efficiently check if a letter exists in the word or the list of previous guesses.
- **Flow Control:** Utilizing `break` to exit the game loop and `continue` to skip specific iterations when a redundant guess is made.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Save the code as `Hangman.py`.
3. Run the script using your terminal or IDE:
   ```bash
   python Hangman.py