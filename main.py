# There will be a gameboard
# There will be two players
# Swap between two players
# Take player inputs
# There will be a winner adn a looser
# There will be player switch
# Looping the game till it is no quit
# check column, row and cross(diagonal)
# check tie



board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

player_cur = "X"
winner = None

run_game = True

# There will be a gameboard
def show_board(board):
    print(board[0]," | ", board[1]," | ", board[2])
    print("------------------")
    print(board[3], " | ", board[4], " | ", board[7])
    print("------------------")
    print(board[6], " | ", board[7], " | ", board[8])


# Take player inputs
def player_input(board):
    user_in = int(input("Enter position: "))
    if user_in>=1 and user_in<=9 and board[user_in-1]=="-":
        board[user_in-1] = player_cur
    else:
        print("The slot is not empty")


#check column
def check_col(board):
    global winner
    if board[0] == board[3]==  board[6]=="X":
        winner=board[0]
        return True
    elif board[1]== board[5]== board[7]=="X":
        winner=board[1]
        return True
    elif board[2]== board[5]== board[8]=="X":
        winner=board[]
        return True


#check rows
def check_row(board):
    global winner
    if board[0]==board[1]==board[2]=="X":
        winner = board[0]
        return True
    elif board[3]==board[4]==board[5]=="X":
        winner = board[3]
        return True
    elif board[6]==board[7]==board[8]=="X":
        winner = board[6]
        return True


#check cross(diagonal)
def check_cross(board):
    global winner

    if board[0]==board[4]==board[8]=="X":
        winner = board[0]
        return True
    elif board[2]==board[4]==board[6]=="X":
        winner = board[2]
        return True


#check tie
def check_tie(board):
    if "-" not in board:
        show_board(board)
        print("It's a tie!!!!")

        run_game = False

# Swap between two players
def player_swap():
    global player_cur

    if player_cur=="X:
        player_cur= "O"
    else:
        player_cur = "X"

#check the winner
def check_final():
    if check_cross(board) or check_row(board) or check_col(board):
        print( )


# Looping the game
while run_game:
    show_board(board)
    player_input(board)


