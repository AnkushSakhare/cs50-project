# cs50p-project
My final project for cs50p python course.

Video Demo: https://youtu.be/E-cztcsWwnw         

# Rock, Paper, Scissors Game


🪨📄✂️ Rock, Paper, Scissors Game
🧾 Overview

This project is a Python-based implementation of the classic hand game Rock, Paper, Scissors. It is designed to be run in the command line or terminal and provides an interactive text-based experience. Players can either compete against the computer, which makes random decisions, or play head-to-head with another person. The program walks the user through each step of the game, ensuring smooth gameplay with clear instructions and robust input validation. The logic used to determine the winner adheres to traditional game rules.

This project is ideal for beginners learning Python and covers many foundational programming concepts in a fun and engaging way.

✨ Features

Two Game Modes:

🎮 Player vs Computer – Play against a randomly acting AI opponent.

🤝 Player vs Player – Two users can compete locally using the same terminal.

Rule Display Option – Players can view the rules at any time from the main menu.

Input Validation – Prevents invalid entries and prompts the user until valid input is given.

Randomized Computer Moves – Utilizes Python’s random.choice() to simulate unpredictability.

Simple, Clean UI – Text-based interface with clear prompts and results.

Play Again Loop – Allows players to replay the game as many times as they like without restarting the program.

Basic Screen Clearing – Simulates hiding Player 1’s choice from Player 2 using newline spacing.

▶️ How to Use

Run the Python script in your terminal:

python project.py


Choose a game mode from the menu:

Enter 1 to play against the computer

Enter 2 to play against another player

Enter 3 to view the game rules

Enter 4 to quit the game

Follow the on-screen prompts to input your choices.

After each round, you’ll be asked whether you want to play again. Enter "yes" or "no" to continue or exit.

🧠 Python Concepts Used

This project demonstrates a solid understanding and practical use of several key programming concepts in Python:

✅ Functions – Modular code with clearly defined purposes

🔄 Loops – while loops for continuous gameplay and input validation

🔀 Random Number Generation – random.choice() for simulating computer choices

🤔 Conditional Logic – if/elif/else statements to evaluate game outcomes

🧮 Global Variables – Shared constants (choices) used across functions

💬 User Input/Output – Interactive command-line communication

🔗 Function Interactions – Functions call and work with one another for cohesive gameplay logic

🛠️ Challenges and Approach

One key challenge was maintaining clean separation between user inputs in Player vs Player mode, where Player 2 should not see Player 1's input. While true screen clearing requires platform-specific commands or libraries, a simple workaround using repeated newlines (\n) was implemented to create a visual buffer.

Another challenge was ensuring robust input validation, which was handled using while loops that re-prompt the user until correct input is entered.

The overall program structure is modular, with reusable functions and a centralized main() loop to manage game flow. This makes the codebase easier to maintain, expand, and debug.

🚀 Future Improvements

Potential enhancements for future versions of this project include:

📊 Score Tracking – Maintain and display running scores across multiple rounds.

🖼️ Graphical User Interface (GUI) – Use libraries like Tkinter or Pygame for a visual game interface.

📝 Game History Logging – Save game results to a file for review or stats.

🤯 Extended Game Variants – Add new moves such as “Lizard” and “Spock” for a more complex and fun experience.

🌍 Online Multiplayer – Use sockets or web technologies to allow remote PvP gameplay.

🎯 Conclusion

This Rock, Paper, Scissors project not only recreates a timeless game but also provides a great opportunity to practice core Python skills. With its clear structure, modular design, and focus on input handling, it serves as a strong foundation for more advanced game development projects in the future.

Let me know if you'd like this formatted for a PDF, GitHub README, or academic report.

Future Improvements       
Possible future additions include:        

Score tracking across multiple rounds       

GUI version using a framework like Tkinter      

Saving game history to a file     

Adding more moves (e.g., “Lizard”, “Spock” variation)     
