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


class DFS():

	def __init__(self, matrix, board_size):
		self.soreted_matrix = np.zeros((board_size, board_size))

		counter = 1

		for i in range(0, board_size):
			for j in range(0, board_size):
				self.soreted_matrix[i][j] = 0
				counter += 1

		self.solution_path = []
		self.soreted_matrix[board_size - 1][board_size - 1] = 0
		self.board_size = board_size
		self.board = matrix
		self.root = node.Node(0, -1, 0)


	def DFS_algorithm(self):

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
			return

		# Visita os nodos e coloca os filhos na lista de nao visitados
		while visited_boards:
			visited_board = visited_boards.pop()

			# Salva os filhos do nodo atual
			current_neighbors = utils.get_random_neighbors(visited_board, self.board_size)
			curr_node = visited_nodes[counter]
			counter += 1

			# Coloca os filhos na lista de nao visitados
			while current_neighbors:

				neighbor = current_neighbors.pop()

				new_node = node.Node(curr_node, visited_board[neighbor[0]][neighbor[1]], curr_node.get_depth()+1)
			
				
				# se o pai e o filho representam movimentos distintos
				if(new_node.get_value() != new_node.get_upper().get_value()):
					visited_nodes.append(new_node)
					not_visited_boards.append(utils.swap_position(visited_board, neighbor))
					curr_node.append_lower(new_node)


				# Visita os nodos ainda nao visitados
				while not_visited_boards:
					not_visited = not_visited_boards.pop()

					if(not np.array_equal(sorted_matrix, not_visited)):
						# coloca not_visited no visited
						visited_boards.append(not_visited)
						for n in utils.get_random_neighbors(not_visited, self.board_size):
							current_neighbors.append(n)
					else:
						new_node = node.Node(curr_node, self.get_last_movement(visited_board), curr_node.get_depth() + 1)
						visited_nodes.append(new_node)
						print("Tabuleiro final")
						print(not_visited)
						#print('Completou puzzle')
						self.solution_path = self.get_solution(new_node)

						return
					curr_node = new_node

		not_visited_boards = []


	def get_last_movement(self, board):
		indexes = np.where(board == 0)
		return sorted_matrix[indexes[0][0]][indexes[1][0]]

	def get_solution(self, curr_node):
		solution = []
		while(curr_node.get_value() != -1):
			solution.append(int(curr_node.get_value()))
			#print(curr_node.get_value())
			curr_node = curr_node.get_upper()
		return list(reversed(solution))

	def get_solution_path(self):
		print(self.board)
		return self.solution_path		

