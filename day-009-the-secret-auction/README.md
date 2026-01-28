# Day 9: The Secret Auction 🔨

This is the ninth project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a "blind auction" program that allows multiple users to enter their names and bids privately. Once all bids are entered, the program determines and announces the winner.

## 📝 Description
In a secret auction, bidders do not know what others have bid. This program facilitates that by collecting names and bid amounts in a loop. After each entry, it clears the screen (using multiple newlines) to hide the previous user's data. Finally, it iterates through the recorded data to find the highest bidder.

## ✨ Features
- **Blind Bidding Privacy:** Prints multiple newlines after each entry to prevent the next user from seeing previous bids.
- **Dynamic Data Storage:** Uses a Python dictionary to store names as keys and bid amounts as values.
- **Continuous Input Loop:** A `while` loop allows an unlimited number of participants to join the auction.
- **Winner Determination Logic:** A custom loop that compares all bids in the dictionary to find the highest value and its associated name.

## 💡 What I Learned
- **Dictionaries:** Storing and retrieving data using key-value pairs (`{name: bid}`).
- **Dictionary Iteration:** Using a `for` loop to look through the keys in a dictionary to find specific information.
- **Comparison Logic:** Initializing a "max value" variable and updating it as the program finds higher numbers.
- **Data Type Casting:** Converting string inputs into integers to perform mathematical comparisons.
- **Console UI:** Using escape characters like `\n` to manage the visual space in the terminal.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Save the code as `TheSecretAuction.py`.
3. Run the script using your terminal or IDE:
   ```bash
   python TheSecretAuction.py