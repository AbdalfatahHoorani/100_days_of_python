# Day 15: Coffee Machine ☕

This is the fifteenth project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a simulation of a real-world coffee machine that handles ingredient inventory, processes coin-based payments, and provides maintenance reports.

## 📝 Description
The program acts as a virtual barista. It offers three types of drinks: Espresso, Latte, and Cappuccino. For every order, the machine checks if it has enough resources (water, milk, and coffee). If resources are sufficient, it prompts the user to insert coins. It calculates the total value of the coins, provides change if necessary, and deducts the used ingredients from the internal inventory.

## ✨ Features
- **Resource Management:** Tracks the levels of water, milk, and coffee. It refuses to make a drink if any ingredient is insufficient.
- **Coin Processing System:** Accepts Quarters, Dimes, Nickles, and Pennies, calculating the total value and validating if it covers the drink cost.
- **Change Calculation:** Automatically calculates and returns change to the user, formatted to two decimal places.
- **Maintenance Report:** A "secret" keyword (`report`) allows an operator to see the current status of the machine's resources and the total money collected.
- **Power Off:** Includes a hidden command (`off`) to safely shut down the program, simulating a physical power switch.

## 💡 What I Learned
- **Nested Dictionaries:** Managing complex data structures to store drink recipes, costs, and current machine resources.
- **Function Orchestration:** Building a chain of logic where one function (`transactionChecker`) coordinates multiple helper functions (`resourceChecker` and `coinProcesser`).
- **Default Parameter Values:** Using default arguments in functions (e.g., `milk=0`) to handle drinks like Espresso that don't require all ingredients.
- **State Maintenance:** Updating a central dictionary (`resources`) to reflect changes in inventory and money over multiple loop iterations.
- **Floating Point Precision:** Formatting output strings using `:.2f` to ensure currency is displayed correctly (e.g., $1.50 instead of $1.5).

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Save the code as `CoffeeMachine.py`.
3. Run the script using your terminal or IDE:
   ```bash
   python CoffeeMachine.py