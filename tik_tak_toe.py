#Tic Tac Toe 
# Import modules 
import os 
import random
import time 

# Clear screen 
os.system("clear") 

# Define board 
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# Draw board 
def draw_board():
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[1], board[2], board[3])) 
    print("   |   |   ") 
    print("-------------") 
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[4], board[5], board[6])) 
    print("   |   |   ") 
    print("-------------") 
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[7], board[8], board[9])) 
    print("   |   |   ") 
    print("-------------")      

    
# Check for a win 
def is_win(choice): 
    combos = [[1,2,3],[4,5,6],[7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]] 
    for combo in combos:
        a = combo[0]
        b = combo[1]
        c = combo[2]
        if board[a] == choice and board[b] == choice and board[c] == choice: 
            return True
    return False

# Check if move is legal 
def is_legal(choice):
    if choice >= 1 and choice <= 9 and board[choice] == " ":
        return True 
    else: 
        return False 
        print("Sorry, that space is not empty.") 
        time.sleep(1)

# check_draw
def is_draw():
    if board.count(" ") == 0: 
        return True 
    else: 
        return False 
        
# Main loop
while True: 
    # Draw the board
    os.system("clear")
    draw_board()
    
    # X's turn
    # Get X's choice
    x_choice = int(input("Which piece of board would you like to put your X in? Please choose 1-9. >"))
    
    if is_legal(x_choice):
        board[x_choice] = "X"

    if is_win("X"):
        print("X wins!")
        break
    elif is_draw(): 
        print("Tie")
        break

    # O's turn
    # Get O's choice
    o_choice = int(input("Which piece of board would you like to put your O in? Please choose 1-9. >"))
    
    if is_legal(o_choice):
        board[o_choice] = "O"

    if is_win("O"):
        print("O wins!")
        break
    elif is_draw(): 
        print("Tie") 
        break

