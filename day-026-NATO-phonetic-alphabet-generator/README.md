# Day 26: NATO Phonetic Alphabet Generator ✈️

This is the twenty-sixth project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a command-line tool that converts any word provided by the user into its corresponding NATO phonetic alphabet code words (e.g., "Hello" becomes ["Hotel", "Echo", "Lima", "Lima", "Oscar"]).

## 📝 Description
The program demonstrates advanced data manipulation techniques in Python. It reads a CSV file containing the alphabet and their respective phonetic codes, transforms that data into a searchable dictionary using dictionary comprehension, and then uses list comprehension to instantly translate a user's input into a list of phonetic codes.

## ✨ Features
- **Data Transformation:** Converts a CSV dataset into a Python dictionary format using `pandas` and dictionary comprehension.
- **Instant Translation:** Uses list comprehension to iterate through a user's string and map each letter to its phonetic equivalent.
- **Case Insensitivity:** Automatically handles lowercase input by converting it to uppercase to match the dataset.
- **Iterative Data Processing:** Showcases the use of `.iterrows()` for efficient row-by-row iteration over a Pandas DataFrame.

## 💡 What I Learned
- **Dictionary Comprehension:** Creating dictionaries from existing data structures in a single, readable line.
- **List Comprehension:** Transforming strings into lists of specific values using a concise syntax.
- **Pandas `.iterrows()`:** Learning how to iterate through a DataFrame while maintaining access to specific row attributes (like `row.letter` and `row.code`).
- **Data Mapping:** Building a "look-up" system where one set of data (alphabet) serves as a key to retrieve another (phonetic code).

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Install the `pandas` library if you haven't already:
   ```bash
   pip install pandas