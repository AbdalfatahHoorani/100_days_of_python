# Day 25: U.S. States Quiz Game 🗺️

This is an interactive educational game built using Python's `turtle` graphics and the `pandas` library. The project challenges the user's geographic knowledge by asking them to name all 50 U.S. states.

## 📝 Description
The program displays a blank map of the United States. As the user types the name of a state into the pop-up prompt, the program checks a CSV dataset for a match. If correct, the state's name is written onto the map at its exact geographic coordinates. If the user decides to quit by typing "Exit", the program generates a new CSV file containing all the states they missed to help them study.

## ✨ Features
- **Graphic Interface:** Uses a custom `.gif` image as the turtle screen background.
- **Dynamic Labeling:** Spawns hidden turtle objects to write text at specific (x, y) coordinates retrieved from a dataset.
- **Smart Data Handling:** Uses `pandas` to read state names and coordinates from `50_states.csv`.
- **Learning Logic:** Utilizes list comprehensions to compare the user's answers against the master list and export the "missed states" for future learning.
- **Input Normalization:** Automatically titles user input (e.g., "alabama" becomes "Alabama") to ensure matches aren't missed due to casing.

## 💡 What I Learned
- **Pandas Data Frames:** How to read CSV files and filter data based on row conditions (e.g., `data[data.state == answer]`).
- **Data Conversion:** Converting Pandas series into standard Python lists using `.to_list()`.
- **Turtle Coordinate System:** Mapping image-based coordinates to the turtle screen.
- **List Comprehension:** Efficiently creating new lists of "missed items" in a single line of code.
- **File Export:** Creating and saving new DataFrames to a `.csv` file.

## 🚀 How to Run
1. Ensure you have `pandas` installed (`pip install pandas`).
2. Ensure `main.py`, `50_states.csv`, and `blank_states_img.gif` are in the same directory.
3. Run the script:
   ```bash
   python main.py