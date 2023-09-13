board = [' 'for x in range(9)]
def print_board():
	row1 = f'{board[0]}_|_{board[1]}_|_{board[2]}'
	row2 = f'{board[3]}_|_{board[4]}_|_{board[5]}'
	row3 = f'{board[6]} | {board[7]} | {board[8]}'
	print()
	print(row1)
	print(row2)
	print(row3)
	print()
def player_move(icon):
	if icon == "X":
		player = 1
	elif icon == "O":
		player = 2
	print(f"Player-{player} turn ({icon}): ")
	choice = int(input("Enter Your Move(1-9): "))
	if board[choice-1] == ' ':
		board[choice-1] = icon
	else:
		print("\n That space is already taken!")
		player_move(icon)
def win_condition(icon):
	if (board[0] == icon and board[1] == icon and board[2] == icon) or\
	(board[3] == icon and board[4] == icon and board[5] == icon) or\
	(board[6] == icon and board[7] == icon and board[8] == icon) or\
	(board[0] == icon and board[3] == icon and board[6] == icon) or\
	(board[1] == icon and board[4] == icon and board[7] == icon) or\
	(board[2] == icon and board[5] == icon and board[8] == icon) or\
	(board[0] == icon and board[4] == icon and board[8] == icon) or\
	(board[2] == icon and board[4] == icon and board[6] == icon):
		return True
	else:
		return False
def is_draw():
	if ' ' not in board:
		return True
	else:
		return False
while True:
	print_board()
	player_move("X")
	print_board()
	if win_condition("X"):
		print("X Wins!")
		break
	elif is_draw():
		print("Draw!")
		break
	player_move("O")
	if win_condition("O"):
		print_board("O")
		print("O Wins!")
		break
	elif is_draw():
		print("Draw!")
		break