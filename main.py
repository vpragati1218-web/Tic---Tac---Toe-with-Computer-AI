import tkinter as tk
import random
from tkinter import messagebox
# Main window
window = tk.Tk()
window.title("Tic-Tac-Toe AI")
title_label = tk.Label(
    window,
    text="🎮 TIC-TAC-TOE",
    font=("Arial",20,"bold"),
    bg="#1E1E2F",
    fg="white"
)
title_label.pack(pady=(10,5))
subtitle_label = tk.Label(
    window,
    text="🤖 AI | 🧑‍🤝‍🧑 Multiplayer",
    font=("Arial",10,"bold"),
    bg="#1E1E2F",
    fg="#B8B8C8"
    )
subtitle_label.pack(pady=(0,8))
board = tk.Frame(
    window,
    bg="#1E1E2F",
    padx=10,
    pady=10)


window.state("zoomed")
window.resizable(True,True)
window.config(bg="#1E1E2F")
# Game board

#Show whose turn it is
turn_label = tk.Label(
    window,
    text="🎮 Your Turn: X",
    font=("Arial",14,"bold"),
    bg="#1E1E2F",
    fg="white"
)
turn_label.pack(pady=(10,3))
#Scoreboard
score_label = tk.Label(
    window,
    text ="🏆 X Wins: 0  O Wins:0  🤝Draws:0",
    font=("Arial",11,"bold"),
    bg="#1E1E2F",
    fg="#FFD166"
 )
score_label.pack(pady=(0,8))
# Current turn
turn = "X"
# Store all 9 buttons
buttons = []
        # Create 3X3 BOARD
for row in range (3):
    for column in range(3):
        button = tk.Button(board,
    text="",
    width=5,
    height=2,
    font=("Arial",20,"bold"),
    relief="ridge",
    bd=3
    )
        #Connect button with player_move function
        button.config(command=lambda b=button: player_move(b))
        # Place button on board
        button.grid(row=row,
                    column=column,
                    padx=5,
                    pady=5)
        # Store button in list
        buttons.append(button)
        #Show the board
board.pack(pady=2)
# Start the program


game_over = False
x_score = 0
o_score = 0
draw_score = 0
game_mode = "AI"
difficulty = "HARD"
#Game mode function
#Select AI mode
def select_ai_mode():
   global game_mode
   global turn
   global game_over
   game_mode = "AI"
   turn = "X"
   game_over = False
   #Clear the board 
   for button in buttons:
       button.config(text="",
                     bg="#2C2C3E",
                     fg="white",
                     )
   turn_label.config(text="🎮 Your Turn: X")
       
   print("AI Mode Selected ")
   
   
   
   #Select Multiplayer mode
def select_multiplayer_mode():
   global game_mode
   global turn
   global game_over
   game_mode = "MULTIPLAYER"
   turn = "X"
   game_over = False
   #Clear the board
   for button in buttons:
       button.config(text="",
                     bg="#2C2C3E",
                     fg="white"
                     )
   turn_label.config(text="🎮 Player 1 Turn: X")
   print("Multiplayer Mode Selected")

        
   #Select AI diffculty
def select_difficulty(level):
    global difficulty
    difficulty = level
    print("Difficulty",difficulty)
    if difficulty == "EASY":
        turn_label.config(text="🟢 Easy AI Selected")
    elif difficulty == "MEDIUM":
        turn_label.config(text="🟡 Medium AI Selected")
    else:
        turn_label.config(text="🔴 Hard AI Selected")    
    

def update_score():
   score_label.config(
        text=f"🏆 X Wins: {x_score} O Wins: {o_score}      Draws: {draw_score}"
 )
def reset_game():
    global x_score, o_score, draw_score
    x_score = 0
    o_score = 0
    draw_score = 0
    update_score()
    new_game()
    
  #Start a new game  
   
def new_game():
    global turn
    global game_over
    #Reset turn
    turn = "X"
    #Reset game status
    game_over = False
    #Clear all 9 buttons
    for button in buttons:
        button.config(
            text="",
            bg="#2C2C3E",
            fg="white"
        )
        
        #Reset turn lable
    if game_mode == "AI":
        turn_label.config(text="🎮 Your Turn: X") 
    else:
        turn_label.config(text="🎮 Player 1 Turn: X")
    
mode_frame= tk.Frame(window,
                     bg="#1E1E2F")
mode_frame.pack(pady=2)   
ai_button = tk.Button(
      mode_frame,
      text="🤖 AI",
      font=("Arial",10,"bold"),
      bg="#6C5CE7",
      fg="white",
      activebackground="#5849C4",
      activeforeground="white",
      relief="flat",
      padx=12,
      pady=5,
      command=select_ai_mode
)
ai_button.pack(side="left",padx=5)
     #Multiplayer button
multi_button = tk.Button(
    mode_frame,
      text="🧑‍🤝‍🧑 Multiplayer",
      font=("Arial",10,"bold"),
      bg="navy",
      fg="white",
      activebackground="white",
      relief="flat",
      padx=12,
      pady=5,
      command=select_multiplayer_mode
   )
multi_button.pack(side="left",padx=5)
#Diffculty label
difficulty_label = tk.Label(
    window,
    text="🤖 AI Diffculty",
    font=("Arial",12,"bold"),
    bg="#1E1E2F",
    fg="white"
)

difficulty_label.pack(pady=(2,1))
#Difficulty buttons
difficulty_frame= tk.Frame(window,
                          bg="#1E1E2F")
difficulty_frame.pack(pady=1)

easy_button = tk.Button(
    difficulty_frame,
    text="🟢 Easy",
    font=("Arial",10,"bold"),
    width=9,
    bg="#27AE60",
    fg="white",
    activebackground="#219150",
    activeforeground="white",
    relief="flat",
    command=lambda: select_difficulty("EASY")
)
#Medium button
easy_button.pack(side="left",padx=3)
medium_button = tk.Button(
    difficulty_frame,
    text="🟡 Medium",
    font=("Arial",10,"bold"),
    width=9,
        bg="#F39C12",
        fg="white",
        activebackground="#D68910",
        activeforeground="white",
        relief="flat",
    command=lambda: select_difficulty("MEDIUM")
)
medium_button.pack(side = "left",padx=3)
#Hard button
hard_button = tk.Button(
    difficulty_frame,
    text="🔴 Hard",
    font=("Arial",10,"bold"),
    width=9,
        bg="#E74C32",
        fg="white",
        activebackground="#C03928",
        activeforeground="white",
        relief="flat",
    command=lambda: select_difficulty("HARD")
)
hard_button.pack(side="left",padx=3)
#New Game Button
control_frame= tk.Frame(window,
                        bg="#1E1E2F"
                        )
control_frame.pack(pady=2)
new_game_button = tk.Button(
    control_frame,
    text="🔄 New Game",
    font=("Arial",10,"bold"),
    width=13,
        bg="#3498D8",
       fg="white",
        activebackground="#2980B9",
        activeforeground="white",
        relief="flat",
    command=new_game
)
new_game_button.pack(side="left",padx=5)
#Reset Score Button
reset_score_button = tk.Button(
    control_frame,
    text="🧹 Reset Score",
    font=("Arial",10,"bold"),
    width=13,
    bg="#8E44AD",
           fg="white",
            activebackground="#71368A",
            activeforeground="white",
            relief="flat",
    command=reset_game
)
reset_score_button.pack(side="left",padx=5)

   

winning_combinations = [
    (0,1,2), #Row 1
    (3,4,5), #Row2
    (6,7,8), #Row3
    (0,3,6), #Column 1
    (1,4,7), #Column 2
    (2,5,8), #Column 3
    (0,4,8), #Diagonal
    (2,4,6)  #Diagonal
    ]
#Check if ther is a winner
def check_winner():
   for a, b, c in winning_combinations:
      if (
         buttons[a]["text"] != ""
         and buttons[a]["text"] == buttons[b]["text"]
         and buttons[b]["text"] == buttons[c]["text"]
      ):
         return buttons[a]["text"]
   return None
def highlight_winner(winner):
   for a, b, c in winning_combinations:
      if (
         buttons[a]["text"] == winner
         and buttons[b]["text"] == winner
         and buttons[c]["text"] == winner
      ):
         buttons[a].config(bg="#2ECC71")
         buttons[b].config(bg="#2ECC71")
         buttons[c].config(bg="#2ECC71")
#Show game result
def show_result(message):
    messagebox.showinfo("Game Over", message)
    
# Check if the board is full
def check_draw():
   return all(button["text"] != "" for button in 
buttons) 
#Easy AI - Random move
def easy_move():
    empty_positions = []
    for i in range(9):
        if buttons[i]["text"] == "":
            empty_positions.append(i)
    if empty_positions:
        return random.choice(empty_positions)
    return None 
# Medium move
def medium_move():
    #Check if computer can win 
    for i in range(9):
        if buttons[i]["text"] == "":
            #Temporarily place O
            buttons[i].config(text="O")
            #Check if O wins
            if check_winner() == "O":
                buttons[i].config(text="")
                
                return i
            #Undo the test move
            buttons[i].config(text="")
    for i in range(9):
         if buttons[i]["text"] == "":
                #Temporarily place X
                buttons[i].config(text="X")
                #Check if X wins
                if check_winner() == "X":
                    buttons[i].config(text="")
                    return i
                #Undo the test move
                buttons[i].config(text="")
            #If no winning or blocking move 
    return easy_move()
    # Implement medium difficulty AI logic

  
# Computer move based on difficulty
def computer_move():
    global game_over,o_score,draw_score

      
    # Find the best move using Minimax
    if difficulty == "EASY":
        best_move = easy_move()
    elif difficulty == "MEDIUM":
        best_move = medium_move()
    else:
        best_move = find_best_move()
        # Make the move
    if best_move is not None:
        buttons[best_move].config( text="O",fg="white",bg="#E74C32")

        # Check if computer has won
        winner = check_winner()

        if winner:
            o_score += 1
            update_score()
            highlight_winner(winner)
            turn_label.config(text="🤖 O Wins!")
            show_result("🤖 Computer Wins!")
            game_over = True
            return
            
            

        # Check for draw
        if check_draw():
            draw_score += 1
            update_score()
            turn_label.config(text="🤝Draw!")
            show_result("🤝Game Draw!")
            game_over = True
            return
        
        #Back to player's turn
         
# Player move
def player_move(button):

    global turn
    global game_over
    global x_score
    global o_score
    global draw_score

    # Do not allow moves after the game is over
    if game_over:
        return

    # Do not allow a move on an occupied button
    if button["text"] != "":
        return

   
    # MULTIPLAYER MODE

    if game_mode == "MULTIPLAYER":

        # X's turn
        if turn == "X":
            button.config(
                text="X",
                fg="white",
                bg="#3498D8"
            )

        # O's turn
        else:
            button.config(
                text="O",
                fg="white",
                bg="#E74C32"
            )

        # Check for a winner
        winner = check_winner()

        if winner:

            if winner == "X":
                x_score += 1
            else:
                o_score += 1

            update_score()
            highlight_winner(winner)

            turn_label.config(
                text=f"🏆 {winner} Wins!"
            )

            show_result(
                f"🏆 {winner} Wins!"
            )

            game_over = True
            return

        # Check for a draw
        if check_draw():

            draw_score += 1
            update_score()

            turn_label.config(
                text="🤝 Draw!"
            )

            show_result(
                "🤝 Game Draw!"
            )

            game_over = True
            return

        # Change the turn
        if turn == "X":
            turn = "O"
            turn_label.config(
                text="🎮 Player 2 Turn: O"
            )
        else:
            turn = "X"
            turn_label.config(
                text="🎮 Player 1 Turn: X"
            )

    
    # AI MODE
    
    else:

        # The player always plays as X
        button.config(
            text="X",
            fg="white",
            bg="#3498D8"
        )

        # Check if the player has won
        winner = check_winner()

        if winner:

            x_score += 1
            update_score()

            highlight_winner(winner)

            turn_label.config(
                text="🏆 X Wins!"
            )

            show_result(
                "🏆 You Win!"
            )

            game_over = True
            return

        # Check for a draw
        if check_draw():

            draw_score += 1
            update_score()

            turn_label.config(
                text="🤝 Draw!"
            )

            show_result(
                "🤝 Game Draw!"
            )

            game_over = True
            return

        # Computer's turn
        turn_label.config(
            text="🤖 Computer's Turn"
        )
        computer_move()
        if not game_over:
            turn_label.config(
                text="🎮 Your Turn: X"
            )


        # If the computer has not ended the game
        
#GET BOARD STATE                
def get_board_state():
   #Return the current state of the board 
   return [button["text"] for button in buttons]   
# Minimax AI algorithm
def minimax(board_state, depth, is_maximizing):
    # Check if there is a winner
    for a, b, c in winning_combinations:

        if (
            board_state[a] != ""
            and board_state[a] == board_state[b]
            and board_state[b] == board_state[c]
        ):

            # Computer wins
            if board_state[a] == "O":
                return 10 - depth

            # Player wins
            elif board_state[a] == "X":
                return depth - 10

    # Check for draw
    if "" not in board_state:
        return 0

    # Computer tries to maximize the score
    if is_maximizing:

        best_score = -1000

        for i in range(9):

            if board_state[i] == "":

                # Try O's move
                board_state[i] = "O"

                score = minimax(
                    board_state,
                    depth + 1,
                    False
                )

                # Undo the test move
                board_state[i] = ""

                best_score = max(best_score, score)

        return best_score

    # Player tries to minimize the computer's score
    else:

        best_score = 1000

        for i in range(9):

            if board_state[i] == "":

                # Try X's move
                board_state[i] = "X"

                score = minimax(
                    board_state,
                    depth + 1,
                    True
                )

                # Undo the test move
                board_state[i] = ""

                best_score = min(best_score, score)

        return best_score
# Find the best move for the computer
def find_best_move():

    # Get the current board state
    board_state = get_board_state()

    # Start with the lowest possible score
    best_score = -1000
    best_move = None

    # Check all 9 board positions
    for i in range(9):

        # Check if the position is empty
        if board_state[i] == "":

            # Try O in this position
            board_state[i] = "O"

            # Calculate the score using Minimax
            score = minimax(
                board_state,
                0,
                False
            )

            # Undo the test move
            board_state[i] = ""

            # Update the best move
            if score > best_score:
                best_score = score
                best_move = i

    # Return the best position
    return best_move
window.mainloop()


