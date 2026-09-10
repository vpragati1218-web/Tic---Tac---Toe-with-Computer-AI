# 🎮 Tic-Tac-Toe with Computer AI

A simple and interactive Tic-Tac-Toe game developed using Python and Tkinter.  
The game allows the player to play against the computer using different AI difficulty levels.

## ✨ Features

- 🎮 Player vs Computer mode
- 🧑‍🤝‍🧑 Multiplayer mode
- 🟢 Easy AI – makes random moves
- 🟡 Medium AI – tries to win and block the player
- 🔴 Hard AI – uses the Minimax algorithm
- 🏆 Automatic winner detection
- 🤝 Automatic draw detection
- 📊 Scoreboard for X Wins, O Wins and Draws
- 🔄 New Game option
- 🧹 Reset Score option
- 🎨 User-friendly graphical interface using Tkinter

## 🛠️ Technologies Used

- Python
- Tkinter
- Random module
- Minimax Algorithm

## 🤖 AI Difficulty Levels

### Easy
The computer selects an empty position randomly.

### Medium
The computer:
1. Checks if it can win.
2. Checks if it needs to block the player's winning move.
3. Otherwise, makes a random move.

### Hard
The computer uses the **Minimax algorithm** to evaluate possible moves and choose the best move.

## ▶️ How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run:

```bash
python main.py
