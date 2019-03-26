import numpy as np
import random

class Shuffle:
    def __init__(self):
        self.matrix = np.zeros((3,3))
        self.zero_pos = [2,2]
        self.moves_list = []

        self.matrix[0][0] = 1
        self.matrix[0][1] = 2
        self.matrix[0][2] = 3
        self.matrix[1][0] = 4
        self.matrix[1][1] = 5
        self.matrix[1][2] = 6
        self.matrix[2][0] = 7
        self.matrix[2][1] = 8
        self.matrix[2][2] = 0

    def shuffle_algorithm(self, n_moves):
        for n in range (n_moves):
            self.moves_list.append(self.swap_positions(self.get_neighbors()))


    def get_neighbors(self):
        if self.matrix[0][0] == 0:
            return [[0,1],[1,0]]
        elif self.matrix[0][1] == 0:
            return [[0,0], [1,1],[0,2]]
        elif self.matrix[0][2] == 0:
            return [[0,1], [1,2]]
        elif self.matrix[1][0] == 0:
            return [[0,0], [1,1], [2,0]]
        elif self.matrix[1][1] == 0:
            return [[0,1], [1,2], [2,1], [1,0]]
        elif self.matrix[1][2] == 0:
            return [[0,2], [1,1], [2,2]]
        elif self.matrix[2][0] == 0:
            return [[1,0,], [2,1]]
        elif self.matrix[2][1] == 0:
            return [[2,0], [1,1], [2,2]]
        elif self.matrix[2][2] == 0:
            return [[2,1], [1,2]]
        else:
            print("Erro: 0 Nao Encontrado")

    def swap_positions(self, n_list):
        pos = n_list[random.randint(0, len(n_list)-1)]
        self.matrix[self.zero_pos[0]][self.zero_pos[1]] = self.matrix[pos[0]][pos[1]]
        self.matrix[pos[0]][pos[1]] = 0
        aux = self.zero_pos
        self.zero_pos = [pos[0],pos[1]]
        #print(self.matrix[aux[0]][aux[1]])
        return int(self.matrix[aux[0]][aux[1]])

    def get_moves_list(self):
        return self.moves_list