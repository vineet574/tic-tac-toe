# tic-tac-toe
# 🎮 Tic-Tac-Toe Game (Python GUI)

A simple **Tic-Tac-Toe** game built using **Python and Tkinter** with a graphical user interface (GUI).  

## 📌 Features
✔️ Simple and Interactive UI  
✔️ Click-based gameplay (No need to type moves!)  
✔️ "X" and "O" color differentiation  
✔️ Automatic winner detection  
✔️ Restart button to reset the game  

## 🖥️ How to Run
### **Step 1: Clone the Repository**

git clone https://github.com/your-username/tic-tac-toe.git
cd tic-tac-toe

Step 2: Run the Python File

python tic_tac_toe_gui.py

Requirements
Python 3.x
Tkinter (Comes pre-installed with Python)



🛠️ Setup Instructions
Download or clone this repository.
Open a terminal in the project directory.
Run python tic_tac_toe_gui.py.


🤝 Contributing
Feel free to fork this repo, improve the game, and submit pull requests! 😊




Key Improvements and Explanations:
Player Choice:

The user can now choose to play as either 'X' or 'O'. This adds a bit of personalization.

Play Against Computer:

The user can choose to play against the computer or against another human player.

Computer AI (Basic):

get_computer_move() function: This is where the computer "thinks". It now has a very basic AI:

Prioritizes Winning: First, it checks if it can win on its next move. If so, it takes that move.

Blocks the Player: If the computer can't win, it checks if the player can win on their next move. If so, it blocks the player.

Center Preference: If the center square is free, the computer takes it (a common strategy).

Random Move: If none of the above apply, the computer chooses a random available move. This prevents the game from getting stuck.

Input Validation:

get_player_move() function: This ensures the user enters valid row and column numbers (0, 1, or 2) and that the chosen cell is empty. It handles ValueError exceptions if the user doesn't enter numbers. This makes the game more robust.

is_board_full() function:

This function checks if all the cells on the board are filled. It's used to determine if the game has ended in a draw.

Clearer Game Flow:

The tic_tac_toe() function is better organized.

How to Play
Run the Python code.

You'll be prompted to choose whether you want to be 'X' or 'O'.

You'll be asked if you want to play against the computer.

If playing against the computer, the computer's moves will be printed.

When it's your turn, enter the row and column numbers (0-2) separated by a space (e.g., "0 0" for the top-left cell).

Further Enhancements (Ideas)
More Advanced AI: Implement a more sophisticated AI using minimax or Monte Carlo Tree Search for a more challenging opponent.

Difficulty Levels: Offer different difficulty levels for the computer AI. Easy could be purely random, medium could use the current logic, and hard could use minimax.

GUI: Create a graphical user interface (GUI) using a library like Tkinter, PyQt, or Pygame to make the game more visually appealing.

Multiplayer (Networked): Allow two players to play against each other over a network.

Scorekeeping: Keep track of the number of wins for each player.

Replay Option: Ask if the players want to play again after a game ends.

Board Size: Allow the user to choose the size of the board (e.g., 4x4, 5x5) for a more complex game. This would require modifying the win-checking logic.
