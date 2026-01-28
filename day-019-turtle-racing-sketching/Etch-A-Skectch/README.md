# Day 19: Etch-A-Sketch ✍️

This is another project from Day 19 of the "100 Days of Code: The Complete Python Pro Bootcamp". It is a classic Etch-A-Sketch clone that allows the user to draw on the screen by controlling the turtle with the keyboard.

## 📝 Description
The program creates an interactive drawing board where the user can move a turtle in four directions and rotate it to create complex shapes. It also includes a reset function to clear the canvas and return the turtle to the starting position, just like shaking a real Etch-A-Sketch.

## ✨ Features
- **Keyboard Controls:** Mapped to standard WASD keys for intuitive movement.
  - `W`: Move Forward
  - `S`: Move Backward
  - `A`: Counter-Clockwise Rotation
  - `D`: Clockwise Rotation
- **Canvas Reset:** Pressing the `C` key clears all drawings and teleports the turtle back to the center (home) of the screen.
- **Real-time Interaction:** Uses event listeners to trigger functions the moment a key is pressed.
- **Fast Rendering:** The turtle speed is set to "fastest" to ensure smooth drawing without delay.

## 💡 What I Learned
- **Event Listeners:** Using `screen.listen()` and `screen.onkey()` to make the program respond to real-time user input.
- **Higher-Order Functions:** Learning how to pass a function as an argument to another function (e.g., passing the `forward` function into `onkey`).
- **Coordinate Reset:** Using `timmy.home()` to reset the position and heading of the turtle without manually calculating the return path.
- **State Clearing:** Using `timmy.clear()` to wipe the screen buffer while keeping the program running.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. The `turtle` module is part of the Python Standard Library.
3. Save the code as `EtchASketch.py`.
4. Run the script using your terminal or IDE:
   ```bash
   python EtchASketch.py