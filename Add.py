borad = 3
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)