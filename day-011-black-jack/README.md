# Day 11: Blackjack House Rules 🃏

This is the eleventh project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a fully functional, text-based version of the classic casino game Blackjack (21), featuring automated dealer logic and dynamic Ace scoring.

## 📝 Description
The program simulates a game of Blackjack between a player and a computer dealer. The goal is to get a hand value as close to 21 as possible without going over (busting). The game handles the complexities of card values, including the "Ace" rule where an 11 can be converted to a 1 if the hand total exceeds 21.

## ✨ Features
- **Dynamic Ace Adjustment:** Includes a custom `AdjustForAce` function that automatically reduces the value of an Ace from 11 to 1 if the player's or dealer's score goes over 21.
- **Automated Dealer AI:** The dealer follows specific logic (`WillDealerHit`), hitting until it reaches at least 17 or attempts to beat the player's current standing score.
- **Dictionary Mapping:** Uses a dictionary to map card names (e.g., "king", "ace") to their respective numerical values.
- **Game State Management:** Tracks multiple hands, totals, and win/loss conditions (Blackjack, Bust, Win, Loss, or Draw).
- **List Comprehensions:** Utilizes concise Python syntax to calculate hand totals efficiently.

## 💡 What I Learned
- **Advanced Logic Flow:** Managing multiple `while` loops to handle the player's turn, the dealer's turn, and the overall game session.
- **Complex Function Design:** Breaking down a large game into smaller, reusable functions like `AdjustForAce` and `WinOrBustOrDraw`.
- **List Comprehension & sum():** Using `sum([cards[c] for c in player_hand])` to quickly calculate values from a dictionary based on list items.
- **Modular Game Loop:** Designing a "Play Again" feature that resets the game state while keeping the terminal interface clean.
- **Abstraction:** Creating a helper function for random card generation to keep the main code readable.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Make sure both `BlackJack.py` and `art.py` are in the same directory.
3. Run the script using your terminal or IDE:
   ```bash
   python BlackJack.py