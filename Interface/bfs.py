import shuffle
import numpy as np
import node
import utils
import copy
import sys


class BFS():
    def __init__(self, matrix, board_size):
        self.sorted_matrix = np.zeros((board_size, board_size))

        counter = 1
        for i in range(0, board_size):
            for j in range(0, board_size):
                self.sorted_matrix[i][j] = counter
                counter += 1
        self.sorted_matrix[board_size - 1][board_size - 1] = 0
        self.board_size = board_size

        self.memory_usage = 0
        self.board = matrix
        self.root = node.Node(0, -1, 0)
        self.solution_path = []

    # Executa o algoritmo e retorna uma lista com os movimentos na arvore
    def BFS_algorithm(self):
        # Nodos nao visitados
        visited_boards = []
        not_visited_boards = []
        visited_nodes = []
        counter = 0
        curr_node = self.root

        # Teste se o tabuleiro de entrada ja esta resolvido
        if (not np.array_equal(self.sorted_matrix, self.board)):
            # visited_board_node = [self.board, curr_node]
            visited_boards = [self.board]
            visited_nodes = [curr_node]
        else:
            return

        # Visita os nodos e coloca os filhos na lista de nao visitados
        for visited_board in visited_boards:
            # Salva os filhos do nodo atual
            current_neighbors = utils.get_neighbors(visited_board, self.board_size)
            curr_node = visited_nodes[counter]
            counter += 1

            # Coloca os filhos na lista de nao visitados
            for neighbor in current_neighbors:
                new_node = node.Node(curr_node, visited_board[neighbor[0]][neighbor[1]], 0)

                # se o pai e o filho representam movimentos distintos
                if (new_node.get_value() != new_node.get_upper().get_value()):
                    visited_nodes.append(new_node)
                    not_visited_boards.append(utils.swap_position(copy.copy(visited_board), neighbor))
                    curr_node.append_lower(new_node)

            # Visita os nodos ainda nao visitados
            for not_visited in not_visited_boards:
                if (not np.array_equal(self.sorted_matrix, not_visited)):
                    # coloca not_visited no visited
                    visited_boards.append(not_visited)
                else:
                    new_node = node.Node(curr_node, self.get_last_movement(visited_board), 0)
                    visited_nodes.append(new_node)
                    # print("Tabuleiro final")
                    # print(not_visited)
                    # print('Completou puzzle')
                    self.solution_path = self.get_solution(new_node)
                    self.memory_usage = self.determine_memory_usage(visited_boards, visited_nodes)
                    # print
                    # print("Movimentos para completar: " + str(self.solution_path))
                    return

            not_visited_boards = []

    def get_last_movement(self, board):
        indexes = np.where(board == 0)
        return self.sorted_matrix[indexes[0][0]][indexes[1][0]]

    def print_nodes(self, visited_nodes):
        for nodo in visited_nodes:
            print('Value: ' + str(nodo.get_value()))

    def get_solution(self, curr_node):
        solution = []
        while (curr_node.get_value() != -1):
            solution.append(int(curr_node.get_value()))
            # print(curr_node.get_value())
            curr_node = curr_node.get_upper()
        return list(reversed(solution))

    def get_solution_path(self):
        # print(self.board)
        return self.solution_path

    def determine_memory_usage(self, boards, nodes):
        return (len(boards) * sys.getsizeof(boards[0]) + len(nodes) * sys.getsizeof(nodes[0])) / 1048576

    def get_memory_usage(self):
        return self.memory_usage

# board = np.zeros((3,3))
#
# board[0][0] = 1
# board[0][1] = 2
# board[0][2] = 3
# board[1][0] = 4
# board[1][1] = 0
# board[1][2] = 6
# board[2][0] = 7
# board[2][1] = 5
# board[2][2] = 8
#
# game = BFS(board)
# game.BFS_algorithm()
