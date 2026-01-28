# Day 8: Caesar Cipher 🔐

This is the eighth project from the "100 Days of Code: The Complete Python Pro Bootcamp". It is a text encryption and decryption tool based on the classic Caesar Cipher technique, where each letter in a message is "shifted" a certain number of places down the alphabet.

## 📝 Description
The program allows users to encode (encrypt) or decode (decrypt) messages. By entering a secret message and a shift number, the program shifts each letter to reveal the hidden text. It is designed to be robust, maintaining symbols, numbers, and spaces while only shifting the letters found in the alphabet.

## ✨ Features
- **Bidirectional Logic:** A single function handles both encoding and decoding by dynamically adjusting the shift direction.
- **Symbol & Space Preservation:** If a user enters a character that isn't in the alphabet (like `!`, `@`, or a space), the program keeps it exactly as it is.
- **Infinite Wraparound:** Uses the modulo operator (`%`) to ensure that even if a user enters a shift number larger than 26, the program continues to cycle through the alphabet correctly.
- **User Interface Loop:** Includes a "restart" feature that asks the user if they want to go again, allowing for multiple encryptions without restarting the script.

## 💡 What I Learned
- **Functions with Inputs:** Creating a single function (`caesar`) that takes multiple arguments (`original_text`, `shift_amount`, and `encode_or_decode`).
- **Modulo Operator Logic:** Using `% len(alphabet)` to prevent "Index Out of Range" errors and handle large shift numbers.
- **Conditional Loops:** Implementing a `while True` loop combined with a `break` statement to create a repeatable program.
- **Data Validation:** Using `.lower()` on inputs to ensure the program remains case-insensitive and doesn't break when comparing strings.
- **Handling Edge Cases:** Writing logic to skip non-alphabetic characters using `if letter in alphabet` checks.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. Save the code as `caeser_cipher.py`.
3. Run the script using your terminal or IDE:
   ```bash
   python caeser_cipher.py