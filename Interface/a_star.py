import numpy as np
import node
import utils
import copy

class A_STAR():
    def __init__(self, matrix, board_size):
        self.board = matrix
        self.board_size = board_size
        self.sorted_matrix = utils.create_sorted_matrix(board_size)
        print(self.sorted_matrix)

    def a_star_algorithm(self):
        pass


matrix = np.zeros((3, 3))
matrix[0][0] = 1
matrix[0][1] = 2
matrix[0][2] = 3
matrix[1][0] = 4
matrix[1][1] = 5
matrix[1][2] = 6
matrix[2][0] = 7
matrix[2][1] = 0
matrix[2][2] = 8
teste = A_STAR(matrix, 3)