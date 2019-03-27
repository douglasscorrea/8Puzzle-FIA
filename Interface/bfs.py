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

# 1 3 8
# 7 0 6
# 2 5 4

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
		# print(self.board)
		# print()
		curr_node = self.root

		# Teste se o tabuleiro de entrada ja esta resolvido
		if(not np.array_equal(sorted_matrix, self.board)):
			# visited_board_node = [self.board, curr_node]
			visited_boards = [self.board]
			visited_nodes = [curr_node]
		else:
			return return_path(curr_node)

		# print(visited_boards)

		# Visita os nodos e coloca os filhos na lista de nao visitados
		# for visited, curr_node in visited_boards, visited_nodes:
		
		# for (visited_board, visited_node) in zip(visited_boards, visited_nodes):
		for visited_board in visited_boards:
			# print("VISITED BOARD")
			# print(visited_board)
			# print
			# Salva os filhos do nodo atual
			current_neighbors = self.get_neighbors(visited_board)
			# print("CURRENT NEIGHBORS")
			# print current_neighbors
			# print
			# print(current_neighbors)
			# Coloca os filhos na lista de nao visitados
			for neighbor in current_neighbors:
				not_visited_boards.append(utils.swap_position(copy.copy(visited_board), neighbor))
			# print(not_visited_boards)
			# Visita os nodos ainda nao visitados
			for not_visited in not_visited_boards:
				# print("NOT VISITED")
				# print(not_visited)
				# print
				if(not np.array_equal(sorted_matrix, not_visited)):
					# coloca not_visited no visited

					# print visited_boards
					visited_boards.append(not_visited)
					new_node = node.Node(curr_node, not_visited[neighbor[0]][neighbor[1]])
					# print(new_node.get_value())
					curr_node.append_lower(new_node)
					visited_nodes.append(new_node)


				else:
					print not_visited
					print('Completou puzzle')
					return
					#return return_path(curr_node)

			not_visited_boards = []
		# for nodes in visited_nodes:
			# print(nodes.get_value())
		# print

		# for b in visited_boards:
		# 	print(b)

	def return_path(self, node):
		curr_node = node
		path = []

		while curr_node.get_value() != -1:
			path.append(curr_node.get_value())
			curr_node = curr_node.get_upper()

		return path


board = np.zeros((3,3))

board[0][0] = 0
board[0][1] = 3
board[0][2] = 7
board[1][0] = 4
board[1][1] = 8
board[1][2] = 6
board[2][0] = 5
board[2][1] = 1
board[2][2] = 2	

game = BFS(board)

#print(game.BFS_algorithm())







