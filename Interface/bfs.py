# -*- coding: utf-8 -*-
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

        self.solution_path = []
        self.board_size = board_size
        self.root = node.Node(0, -1, 0)
        self.root.set_board(matrix)
        self.max_nodes = 0
        self.memory_usage = 0

    def BFS_algorithm(self):
        not_visited_nodes = [self.root]
        
        while not_visited_nodes:
            if self.max_nodes < len(not_visited_nodes):
                self.max_nodes = len(not_visited_nodes)
            current_node = not_visited_nodes.pop(0)

            if np.array_equal(np.array(current_node.get_board()), np.array(self.sorted_matrix)):
                #print("Tabuleiro final")
                #print(current_node.get_board())
                #print('Completou puzzle')
                self.solution_path = self.get_solution(current_node)
                self.memory_usage = self.determine_memory_usage(not_visited_nodes)
                #print("Movimentos para completar: " + str(self.solution_path))
                return
            else:
                if current_node.get_depth() <= 31:
                    #Pega todos os visinhos possiveis
                    neighbors = utils.get_neighbors(current_node.get_board(), self.board_size)

                    #laço para percorrer os possiveis vizinhos e adicionar na lista de nao visitados
                    for neighbor in neighbors:
                        if current_node.get_value() == -1:
                            new_board = utils.swap_position(copy.copy(current_node.get_board()), neighbor)
                            new_node = node.Node(current_node, current_node.get_board()[neighbor[0],neighbor[1]], current_node.get_depth() + 1)
                            new_node.set_board(new_board)
                            not_visited_nodes.append(new_node)

                        elif current_node.get_value() != current_node.get_board()[neighbor[0],neighbor[1]]:
                            #print ("value 1 " + str(current_node.get_value()) + " Value 2 " + str(current_node.get_board()[neighbor[0],neighbor[1]]))
                            new_board = utils.swap_position(copy.copy(current_node.get_board()), neighbor)
                            new_node = node.Node(current_node, current_node.get_board()[neighbor[0],neighbor[1]], current_node.get_depth() + 1)
                            new_node.set_board(new_board)
                            not_visited_nodes.append(new_node)
       
                    


    def get_last_movement(self, board):
        indexes = np.where(board == 0)
        return self.sorted_matrix[indexes[0][0]][indexes[1][0]]

    def get_solution(self, curr_node):
        solution = []
        while (curr_node.get_value() != -1):
            solution.append(int(curr_node.get_value()))
            curr_node = curr_node.get_upper()
        return list(reversed(solution))

    def get_solution_path(self):
        return self.solution_path

    def determine_memory_usage(self, nodes):
        return (self.max_nodes * sys.getsizeof(self.root))

    def get_memory_usage(self):
        return self.memory_usage