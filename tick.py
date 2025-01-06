# Tic-Tac-Toe Game in Python

# Function to print the current board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check for a winner
def check_winner(board, player):
    # Winning combinations (row, column, diagonal)
    win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                     (0, 4, 8), (2, 4, 6)]  # Diagonals
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Main function to play the game
def play_game():
    board = [' '] * 9  # Initialize empty board
    current_player = 'X'  # Player X starts

    while True:
        print_board(board)  # Print the board
        # Get valid player input
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move! Please try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        # Make the move
        board[move] = current_player

        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for draw (board is full)
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
