# cs50p-project
My final project for cs50p python course.

Video Demo: https://youtu.be/E-cztcsWwnw         

# Rock, Paper, Scissors Game

## Overview

This project is a Python-based implementation of the classic game Rock, Paper, Scissors. It allows users to play either against the computer or against another player. The game is entirely text-based and runs in the command line or terminal. The program guides the user through the game, validates input, and determines the winner based on standard game rules.

## Features

- Two game modes:
  - **Player vs Computer**
  - **Player vs Player**
- Input validation to ensure players enter valid choices
- Randomized computer moves using Python’s `random` module
- A simple, clear display of choices and results
- An option to view the game rules
- A loop that allows players to continue playing until they choose to quit

## How to Use

1. Run the Python script:
   ```bash
   python project.py
Choose a game mode from the menu:

Enter 1 to play against the computer

Enter 2 to play against another player

Enter 3 to see the rules

Enter 4 to quit

Follow the prompts to input choices. After each round, you'll be asked if you'd like to play again.

Python Concepts Used
This project demonstrates the use of:

Functions (modular design)

Conditional statements (if, elif, else)

Loops (while)

Input validation

Random number generation (random.choice)

Global variables

Multi-function interaction

User interaction via standard input/output

Challenges and Approach
One challenge in the development was ensuring input was always valid and that the screen was “cleared” between Player 1 and Player 2 input in PvP mode. This was handled using newline repetition as a basic form of screen separation. The program is structured using clear, top-level functions and a main() function to organize gameplay flow. This approach keeps the code modular, readable, and testable.

Future Improvements
Possible future additions include:

Score tracking across multiple rounds

GUI version using a framework like Tkinter

Saving game history to a file

Adding more moves (e.g., “Lizard”, “Spock” variation)
