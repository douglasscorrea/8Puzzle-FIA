import numpy as np

def swap_position(board, indexes):
    zero_pos = np.where(board == 0)

    board[zero_pos] = board[indexes]
    board[indexes] = 0

    new_board = board
    return new_board


# Retorna uma Lista com os possiveis vizinhos do 0
def get_neighbors(board, nmax):
    zero_pos = []
    neighbors_list = []
    for i in range(0, nmax):
        for j in range(0, nmax):
            if board[i][j] == 0:
                zero_pos = [i, j]

    i, j = zero_pos[0], zero_pos[1]
    if i-1 >= 0:
        neighbors_list.append([i-1,j])
    if i+1 < nmax:
        neighbors_list.append([i+1,j])
    if j-1 >=0:
        neighbors_list.append([i,j-1])
    if j+1 < nmax:
        neighbors_list.append([i,j+1])

    return neighbors_list
