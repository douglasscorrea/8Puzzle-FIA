import numpy as np
import node
import utils
import copy

class A_STAR():
    def __init__(self, matrix, board_size):
        self.board = matrix  # Matriz de entrada
        self.board_size = board_size  # Dimensao Matriz
        self.sorted_matrix = utils.create_sorted_matrix(board_size)  # Matriz solucionada
        self.root = node.Node(0, -1, 0, self.board)  # No raiz
        self.solution_path = None # Caminho da solucao

    def a_star_algorithm(self, f):
        open_nodes = [self.root]

        while True:
            curr_node = self.get_minor_node(open_nodes)

            if np.array_equal(curr_node.get_board(), self.sorted_matrix):
                self.solution_path = utils.get_solution(curr_node)
                return

            neighbors = utils.get_neighbors(curr_node.get_board(), self.board_size)
            for neighbor in neighbors:
                new_board = utils.swap_position(copy.copy(curr_node.get_board()), neighbor)
                new_node = node.Node(curr_node, curr_node.get_board()[neighbor[0]][neighbor[1]], curr_node.get_depth()+1, new_board)
                new_node.set_h_cost(f(new_node.get_board(), self.board_size))
                if(new_node.get_value() != new_node.get_upper().get_value()):
                    open_nodes.append(new_node)


    # @param nodes = lista de nos abertos
    # @return Retorna o no com menor custo
    def get_minor_node(self, nodes):
        minor_node = nodes[0]
        minor_index = None
        i=0
        for node in nodes:
            if node.get_h_cost() + node.get_depth() <= minor_node.get_h_cost() + minor_node.get_depth():
                minor_node = node
                minor_index = i
            i += 1
        del(nodes[minor_index])
        return minor_node


    def get_solution_path(self):
        return self.solution_path

matrix = np.zeros((3, 3))
matrix[0][0] = 0
matrix[0][1] = 6
matrix[0][2] = 7
matrix[1][0] = 4
matrix[1][1] = 8
matrix[1][2] = 1
matrix[2][0] = 5
matrix[2][1] = 3
matrix[2][2] = 2
teste = A_STAR(matrix, 3)
teste.a_star_algorithm(utils.diff_heuristic)
print(teste.get_solution_path())
