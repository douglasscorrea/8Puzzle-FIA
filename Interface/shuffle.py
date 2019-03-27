import numpy as np
import random
import utils

class Shuffle:
    def __init__(self, nmax):
        self.nmax = nmax
        self.matrix = np.zeros((self.nmax,self.nmax))
        self.zero_pos = []
        self.moves_list = []
        self.reset_shuffle_algorithm()

    def reset_shuffle_algorithm(self):
        self.zero_pos = [self.nmax-1, self.nmax-1]
        self.moves_list = []
        # Preenche Matriz Corretamente
        count = 1
        for i in range(0, self.nmax):
            for j in range(0, self.nmax):
                self.matrix[i][j] = count
                count += 1
        self.matrix[self.nmax-1][self.nmax-1] = 0

    def shuffle_algorithm(self, n_moves):
        self.reset_shuffle_algorithm()
        for n in range(n_moves):
            self.moves_list.append(self.swap_positions(utils.get_neighbors(self.matrix, self.nmax)))

    def swap_positions(self, n_list):
        pos = n_list[random.randint(0, len(n_list)-1)]
        self.matrix[self.zero_pos[0]][self.zero_pos[1]] = self.matrix[pos[0]][pos[1]]
        self.matrix[pos[0]][pos[1]] = 0
        aux = self.zero_pos
        self.zero_pos = [pos[0],pos[1]]
        return int(self.matrix[aux[0]][aux[1]])

    def get_moves_list(self):
        return self.moves_list

    def get_matrix(self):
        return self.matrix