import shuffle
import numpy as np
import node
import utils
import copy

sorted_matrix = np.zeros((3,3))
sorted_matrix[0][0] = 1
sorted_matrix[0][1] = 2
sorted_matrix[0][2] = 3
sorted_matrix[1][0] = 4
sorted_matrix[1][1] = 5
sorted_matrix[1][2] = 6
sorted_matrix[2][0] = 7
sorted_matrix[2][1] = 8
sorted_matrix[2][2] = 0

class BFS():
	def __init__(self, matrix):
		self.board = matrix
		self.root = node.Node(0, -1)
		self.moves_list = self.BFS_algorithm()

	# Retorna uma lista com os indices dos vizinhos [[i,j], [i,j], ...]
	def get_neighbors(self, board):
		if board[0][0] == 0:
			return [[0,1],[1,0]]
		elif board[0][1] == 0:
			return [[0,0], [1,1],[0,2]]
		elif board[0][2] == 0:
			return [[0,1], [1,2]]
		elif board[1][0] == 0:
			return [[0,0], [1,1], [2,0]]
		elif board[1][1] == 0:
			return [[0,1], [1,2], [2,1], [1,0]]
		elif board[1][2] == 0:
			return [[0,2], [1,1], [2,2]]
		elif board[2][0] == 0:
			return [[1,0,], [2,1]]
		elif board[2][1] == 0:
			return [[2,0], [1,1], [2,2]]
		elif board[2][2] == 0:
			return [[2,1], [1,2]]
		else:
			print("Erro: 0 Nao Encontrado")

    # Executa o algoritmo e retorna uma lista com os movimentos na arvore
	def BFS_algorithm(self):
		# Nodos nao visitados
		visited_boards = []
		not_visited_boards = []
		visited_nodes = []
		counter = 0
		curr_node = self.root

		# Teste se o tabuleiro de entrada ja esta resolvido
		if(not np.array_equal(sorted_matrix, self.board)):
			# visited_board_node = [self.board, curr_node]
			visited_boards = [self.board]
			visited_nodes = [curr_node]
		else:
			return return_path(curr_node)

		# Visita os nodos e coloca os filhos na lista de nao visitados
		for visited_board in visited_boards:
			# Salva os filhos do nodo atual
			current_neighbors = self.get_neighbors(visited_board)
			curr_node = visited_nodes[counter]
			counter += 1

			# Coloca os filhos na lista de nao visitados
			for neighbor in current_neighbors:
				new_node = node.Node(curr_node, visited_board[neighbor[0]][neighbor[1]])

				# se o pai e o filho representam movimentos distintos
				if(new_node.get_value() != new_node.get_upper().get_value()):
					visited_nodes.append(new_node)
					not_visited_boards.append(utils.swap_position(copy.copy(visited_board), neighbor))
					curr_node.append_lower(new_node)

			# Visita os nodos ainda nao visitados
			for not_visited in not_visited_boards:
				if(not np.array_equal(sorted_matrix, not_visited)):
					# coloca not_visited no visited
					visited_boards.append(not_visited)
				else:
					new_node = node.Node(curr_node, self.get_last_movement(visited_board))
					visited_nodes.append(new_node)
					print("Tabuleiro final")
					print(not_visited)
					#print('Completou puzzle')
					solution_path = self.get_solution(new_node)
					print
					print("Movimentos para completar: " + str(solution_path))
					return solution_path

			not_visited_boards = []

	def get_last_movement(self, board):
		indexes = np.where(board == 0)
		return sorted_matrix[indexes[0][0]][indexes[1][0]]


	def print_nodes(self, visited_nodes):
		for nodo in visited_nodes:
			print('Value: ' + str(nodo.get_value()))


	def get_solution(self, curr_node):
		solution = []
		while(curr_node.get_value() != -1):
			solution.append(int(curr_node.get_value()))
			#print(curr_node.get_value())
			curr_node = curr_node.get_upper()
		return list(reversed(solution))			

board = np.zeros((3,3))

board[0][0] = 1
board[0][1] = 2
board[0][2] = 3
board[1][0] = 0
board[1][1] = 4
board[1][2] = 6
board[2][0] = 7
board[2][1] = 5
board[2][2] = 8	

game = BFS(board)








