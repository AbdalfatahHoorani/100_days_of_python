# Day 10: Calculator 🧮

This is the tenth project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a functional command-line calculator that performs basic arithmetic operations including addition, subtraction, multiplication, and division.

## 📝 Description
The program provides a simple interface for performing mathematical calculations. It uses a modular approach by defining separate functions for each math operation and utilizes a loop to allow the user to perform multiple calculations in one session. It also features a custom ASCII art logo upon startup.

## ✨ Features
- **Modular Math Functions:** Uses dedicated functions (`add`, `subtract`, `multiplication`, `divide`) to handle logic separately from the main program flow.
- **ASCII Art Integration:** Imports and displays a professional calculator logo from a separate `art.py` file.
- **Continuous Calculation:** Uses a `while` loop to let users perform new calculations without having to restart the script manually.
- **Dynamic User Input:** Collects the desired operation and two numbers from the user to provide an immediate result.

## 💡 What I Learned
- **Functions with Return Values:** Practiced writing functions that `return` a result to the caller, a fundamental concept in building reusable code.
- **Module Imports:** Learned how to organize a project into multiple files (e.g., `art.py` and `calculator.py`) and import data between them.
- **Control Flow:** Using `if/elif` statements to map user strings to specific function calls.
- **Nested Logic:** Managing a `while` loop combined with conditional statements and function execution.
- **Code Organization:** Separating the visual assets (ASCII art) from the functional logic to keep the main script clean.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Make sure both `calculator.py` and `art.py` are in the same directory.
3. Run the script using your terminal or IDE:
   ```bash
   python calculator.py