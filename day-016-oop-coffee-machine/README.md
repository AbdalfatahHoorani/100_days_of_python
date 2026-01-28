# Day 16: OOP Coffee Machine ☕🤖

This is the sixteenth project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a refactored version of the previous Coffee Machine project, rebuilt entirely using Object-Oriented Programming (OOP) principles to demonstrate modularity and code organization.

## 📝 Description
The program performs the same functions as the Day 15 version—managing resources, processing coins, and serving coffee—but it is structured using four distinct classes: `MenuItem`, `Menu`, `CoffeeMaker`, and `MoneyMachine`. This approach demonstrates how to build complex systems by breaking them down into independent, reusable objects that communicate with each other.

## ✨ Features
- **Class-Based Architecture:** Logic is divided into specialized classes, making the code easier to maintain and scale.
- **Encapsulated Data:** Each object manages its own state (e.g., the `MoneyMachine` handles profit, while the `CoffeeMaker` handles ingredient levels).
- **Abstracted Main Logic:** The `main.py` file is significantly shorter and more readable, focusing on coordinating objects rather than manual dictionary manipulation.
- **Robust Menu System:** The `Menu` class dynamically generates a list of available drinks and handles search functionality for specific `MenuItem` objects.

## 💡 What I Learned
- **Classes and Objects:** How to define classes and instantiate objects to represent real-world entities.
- **Attributes and Methods:** Using attributes to store data within an object and methods to define the behaviors that the object can perform.
- **Object Interaction:** Learning how to pass an object (like a `MenuItem`) as an argument to a method of another object (like `coffee_maker.is_resource_sufficient(drink)`).
- **Separation of Concerns:** Dividing a program into distinct sections, where each section addresses a separate part of the functionality (Money, Brewing, Menu).
- **Code Reusability:** Understanding how classes can be written once and used multiple times to create different instances.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Ensure the following files are in the same directory:
   - `main.py`
   - `coffee_maker.py`
   - `menu.py`
   - `money_machine.py`
3. Run the script using your terminal or IDE:
   ```bash
   python main.py