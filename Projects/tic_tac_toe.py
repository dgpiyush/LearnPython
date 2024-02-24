# create a tic tac toe game for me 

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

def get_free_positions(board):
    free_positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_positions.append((i, j))
    return free_positions

def make_move(board, position, player):
    x, y = position
    if board[x][y] == " ":
        board[x][y] = player
        return True
    return False



def position_to_index(position):
    position = int(position) - 1  # Subtract 1 to convert position to zero-based index
    row = position // 3  # Calculate the row index
    col = position % 3   # Calculate the column index
    return row, col

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    player_choice = input("Choose your symbol (X/0): ").upper()
    if player_choice not in ["X", "0"]:
        print("Invalid choice. Defaulting to 'X'.")
        player_choice = "X"
    current_player = player_choice
    winner = None

    while True:
        print_board(board)
        try:
            position = input(f"Player {current_player}, enter your move as position: ")
            row, col = position_to_index(position)
            if (row, col) not in get_free_positions(board):
                print("This position is already taken or out of bounds. Choose another one.")
                continue
        except ValueError:
            print("Invalid input. Please enter row and column as two numbers separated by a comma.")
            continue

        if make_move(board, (row , col ), current_player):
            if check_winner(board, current_player):
                winner = current_player
                break
            elif not get_free_positions(board): # No more free positions, it's a tie
                break
            current_player = "0" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    print_board(board)
    if winner:
        print(f"Congratulations! Player {winner} wins!")
    else:
        print("It's a tie!")

# Start the game
tic_tac_toe()


