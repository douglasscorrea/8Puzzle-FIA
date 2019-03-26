import numpy np as np

def swap_position(board, indexes):
	zero_pos = np.where(board == 0)

	board[zero_pos] = board[indexes]
	board[indexes] = 0

	new_board = board
	
	return new_board