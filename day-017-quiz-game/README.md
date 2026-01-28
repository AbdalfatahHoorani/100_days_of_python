# Day 17: Quiz Game 🧠

This is the seventeenth project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a text-based trivia game that utilizes Object-Oriented Programming (OOP) to manage a question bank and the overall game logic.

## 📝 Description
The Quiz Game pulls computer science-themed trivia questions from a data source and presents them to the player. The program is built using a modular architecture where raw dictionary data is converted into specific `Question` objects. A `QuizBrain` object then manages the flow of the game, including tracking the current question, checking user input, and maintaining a live score.

## ✨ Features
- **Object-Oriented Data Modeling:** Uses a `Question` class to represent each piece of trivia, ensuring data consistency.
- **Dynamic Quiz Engine:** The `QuizBrain` class handles the heavy lifting, including question progression and answer validation.
- **Score Tracking:** Provides immediate feedback after every guess and keeps a running total of the player's performance.
- **Automated Termination:** The program automatically detects when the question bank is empty and provides a final summary.
- **Data Parsing:** Demonstrates how to iterate through a list of dictionaries to create a list of custom objects (`question_bank`).

## 💡 What I Learned
- **Creating Custom Classes:** Practiced defining classes with attributes and methods to build a more organized system.
- **The __init__ Method:** Deepened my understanding of how constructors initialize an object's state.
- **Abstraction:** Learned how to hide the complexity of the quiz logic (like checking if the quiz is over) inside a method (`stillHasQuestions`).
- **Parsing External Data:** Converting raw, structured data (dictionaries) into a list of object instances for more powerful manipulation.
- **Inter-object Communication:** Coordinating different parts of the program so that the main loop only interacts with the high-level `QuizBrain` interface.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Ensure the following files are in the same directory:
   - `main.py`
   - `data.py`
   - `question_model.py`
   - `quiz_brain.py`
3. Run the script using your terminal or IDE:
   ```bash
   python main.py