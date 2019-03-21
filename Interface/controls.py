import numpy as np
import constants as c

class Game_Controls:
    def __init__(self):
        self.algorithm = 0
        self.pos_matrix = np.matrix([[1, 2.3], [4, 5, 6], [7, 8, 0]])

    def enable_algorithm(self, cod):  # 0=none, 1=BFS, 2=DFS, 3=it_DFS, 4=A*H1, 5=A*H2
        self.algorithm = cod
