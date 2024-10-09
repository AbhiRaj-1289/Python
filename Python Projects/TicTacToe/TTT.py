# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all([spot == player for spot in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full
def check_full(board):
    return all([spot != ' ' for row in board for spot in row])

# Main function to play Tic-Tac-Toe
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize the 3x3 board with empty spaces
    current_player = 'X'  # Player X starts first
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Get the player's move
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2) separated by a space: ").split())
        except ValueError:
            print("Invalid input! Please enter two numbers separated by space.")
            continue
        
        if row not in range(3) or col not in range(3):
            print("Invalid position! Please enter row and column between 0 and 2.")
            continue
        
        if board[row][col] != ' ':
            print("Position already taken! Try another.")
            continue
        
        # Place the player's symbol on the board
        board[row][col] = current_player
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the game is a tie
        if check_full(board):
            print_board(board)
            print("The game is a tie!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_game()
