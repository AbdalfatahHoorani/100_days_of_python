# Day 14: Higher Lower Game 🔼🔽

This is the fourteenth project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a comparison game where players must guess which of two famous entities has a higher follower count on Instagram.

## 📝 Description
The program presents the user with two choices from a dataset containing names and descriptions of celebrities, brands, and organizations. The user must decide who has the larger following. If they guess correctly, their score increases, and the winner of the previous round becomes the first option for the next round. The game continues until the user makes an incorrect guess.

## ✨ Features
- **Dynamic Data Sourcing:** Imports a large list of entities from an external `game_data.py` file.
- **Redundancy Protection:** Includes a custom `AlreadyAskedAbout` function and a tracking list to ensure the same entity isn't picked twice in a row.
- **Continuous Gameplay:** If the player is correct, the winner stays for the next round, and a new opponent is randomly selected.
- **Score Tracking:** Keeps a running total of correct guesses and displays it when the game ends.
- **Replay System:** Allows the user to reset the score and start a fresh game without exiting the script.

## 💡 What I Learned
- **Global Variables:** Using the `global` keyword to modify state variables across different functions.
- **List-Based Memory:** Implementing a list (`asked_about`) to track previous indices and prevent repetitive questions.
- **Index Validation:** Creating a `while` loop logic (`NotEqual`) to ensure that two different entities are always compared.
- **Dictionary Access:** Retrieving specific values (name, description, follower count) from nested dictionaries within a list.
- **Game Flow Management:** Designing logic where the "winner" of one round moves into the "Pick One" slot for the next round, maintaining game continuity.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Make sure both `HighVsLow.py` and `game_data.py` are in the same directory.
3. Run the script using your terminal or IDE:
   ```bash
   python HighVsLow.py