# Day 18: Turtle Graphics Art 🎨

This is the eighteenth project from the "100 Days of Code: The Complete Python Pro Bootcamp". It explores the `turtle` graphics module to create various geometric shapes, random walks, spirographs, and a million-dollar "Hirst" style spot painting.

## 📝 Description
This project is divided into two main parts. The first part focuses on mastering the `turtle` library by creating algorithms to draw polygons, dashed lines, and a "random walk" that generates unpredictable paths. The second part (the "Hirst Painting") uses a list of RGB colors extracted from an image to create a 10x10 grid of colored dots, simulating the famous contemporary art style.

## ✨ Features
- **Hirst Dot Painting:** A script that uses coordinate management to draw a 10x10 grid of perfectly spaced colored circles.
- **Dynamic Polygons:** A function that automatically calculates the exterior angles needed to draw any shape from a triangle up to a nonagon ($360 / \text{sides}$).
- **Random Walk Simulator:** A script that moves the turtle in random directions (90° turns) with a random RGB color and increased pen thickness for a modern art effect.
- **Spirograph Generator:** Uses angular math to draw overlapping circles that rotate slightly each time, creating a complex geometric pattern.
- **RGB Color Extraction:** Includes commented-out logic for using the `colorgram` library to extract real color palettes from `.jpg` files.

## 💡 What I Learned
- **Turtle Mechanics:** Deepening knowledge of the `turtle` library, including pen states (`penup`/`pendown`), heading management, and speed controls.
- **Randomness in Art:** Using `random.choice()` and `random.randint()` to create non-deterministic visual outputs.
- **Coordinate Geometry:** Manually calculating x/y movements to reset the turtle's position for new lines in a grid.
- **Tuples & Color Modes:** Working with RGB tuples and setting the screen `colormode` to 255 for full-color spectrum control.
- **Looping Patterns:** Utilizing nested `for` loops to create grids and `while` loops for continuous random movement.

## 🚀 How to Run
1. Ensure you have Python installed on your machine.
2. The `turtle` module is part of the Python Standard Library, so no extra installation is required for the graphics.
3. Save the code as `main.py`.
4. Run the script using your terminal or IDE:
   ```bash
   python main.py