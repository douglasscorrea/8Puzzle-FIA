import time
import shuffle
import bfs
import dfs
import it_dfs
import a_star
import utils

board_size = 3
test_number = 25
shuffle_number = [10, 50, 100, 250, 500, 1000]
shuffler = shuffle.Shuffle(board_size)
boards = [[0 for x in range(test_number)] for y in range(len(shuffle_number))] 

def generate_boards():
	for _ in range(30):
		shuffler.shuffle_algorithm(10)
		boards10.append(shuffler.get_matrix())

	for _ in range(30):
		shuffler.shuffle_algorithm(50)
		boards50.append(shuffler.get_matrix())

	for _ in range(30):
		shuffler.shuffle_algorithm(100)
		boards100.append(shuffler.get_matrix())

	for _ in range(30):
		shuffler.shuffle_algorithm(250)
		boards250.append(shuffler.get_matrix())

	for _ in range(30):
		shuffler.shuffle_algorithm(500)
		boards500.append(shuffler.get_matrix())

	for _ in range(30):
		shuffler.shuffle_algorithm(1000)
		boards1000.append(shuffler.get_matrix())

	print(len(boards10))
	print(len(boards50))
	print(len(boards100))
	print(len(boards250))
	print(len(boards500))
	print(len(boards1000))
def generate_boards2():
	for i in range(len(shuffle_number)):
		for j in range(test_number):
			shuffler = shuffle.Shuffle(board_size)
			shuffler.shuffle_algorithm(shuffle_number[i])
			boards[i][j] = shuffler.get_matrix()

def test_bfs():
	with open('/home/douglascorrea/FIA/BFS.csv', 'wb') as file:
		for moves_number in shuffle_number:
			file.write(str(moves_number) + '\n')
			file.write(' ' + ',')
			print("Moves Number: " + str(moves_number))
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			for i in range (0, test_number):
				print(i)
				shuffler.shuffle_algorithm(moves_number)
				bfs_alg = bfs.BFS(shuffler.get_matrix(), board_size)

				start = time.time()
				bfs_alg.BFS_algorithm()
				end = time.time()

				times.append(end - start)
				memory.append(bfs_alg.get_memory_usage())

			for t in times:
				file.write(str(t) + ',')
				average_time +=  t
			file.write(str(average_time/10) + '\n' + ' ,')
			for m in memory:
				file.write(str(m) + ',')
				average_memory += m
			file.write(str(average_memory/10) + '\n')
def test_dfs():
	with open('/home/douglascorrea/FIA/DFS.csv', 'wb') as file:
		for moves_number in shuffle_number:
			file.write(str(moves_number) + '\n')
			file.write(' ' + ',')
			print("Moves Number: " + str(moves_number))
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			for i in range (0, test_number):
				print(i)
				shuffler.shuffle_algorithm(moves_number)
				dfs_alg = dfs.DFS(shuffler.get_matrix(), board_size)

				start = time.time()
				dfs_alg.DFS_algorithm()
				end = time.time()

				times.append(end - start)
				memory.append(dfs_alg.get_memory_usage())

			for t in times:
				file.write(str(t) + ',')
				average_time +=  t
			file.write(str(average_time/10) + '\n' + ' ,')
			for m in memory:
				file.write(str(m) + ',')
				average_memory += m
			file.write(str(average_memory/10) + '\n')
def test_idfs():
	with open('/home/douglascorrea/FIA/iDFS.csv', 'wb') as file:
		for moves_number in shuffle_number:
			file.write(str(moves_number) + '\n')
			file.write(' ' + ',')
			print("Moves Number: " + str(moves_number))
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			for i in range (0, test_number):
				print(i)
				shuffler.shuffle_algorithm(moves_number)
				print(shuffler.get_matrix())
				dfs_it_alg = it_dfs.IT_DFS(shuffler.get_matrix(), board_size)

				start = time.time()
				dfs_it_alg.IT_DFS_algorithm()
				end = time.time()

				times.append(end - start)
				memory.append(dfs_it_alg.get_memory_usage())

			for t in times:
				file.write(str(t) + ',')
				average_time +=  t
			file.write(str(average_time/10) + '\n' + ' ,')
			for m in memory:
				file.write(str(m) + ',')
				average_memory += m
			file.write(str(average_memory/10) + '\n')
def test_a_star1():
	with open('/home/douglascorrea/FIA/a_star1.csv', 'wb') as file:
		for moves_number in shuffle_number:
			file.write(str(moves_number) + '\n')
			file.write(' ' + ',')
			print("Moves Number: " + str(moves_number))
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			for i in range (0, test_number):
				print(i)
				shuffler.shuffle_algorithm(moves_number)
				print(shuffler.get_matrix())
				a_star_alg = a_star.A_STAR(shuffler.get_matrix(), board_size)

				start = time.time()
				a_star_alg.a_star_algorithm(utils.chessboard_heuristic)
				end = time.time()

				times.append(end - start)
				memory.append(a_star_alg.get_memory_usage())

			for t in times:
				file.write(str(t) + ',')
				average_time +=  t
			file.write(str(average_time/10) + '\n' + ' ,')
			for m in memory:
				file.write(str(m) + ',')
				average_memory += m
			file.write(str(average_memory/10) + '\n')
def test_a_star2():
	with open('/home/douglascorrea/FIA/a_star2_test.csv', 'wb') as file:
		times = []
		memory = []
		average_time = 0
		average_memory = 0
		for i in range(len(shuffle_number)):
			print("Moves: " + str(shuffle_number[i]))
			for j in range(test_number):
				print(j)
				print(boards[i][j])
				a_star_alg = a_star.A_STAR(boards[i][j], board_size)
				start = time.time()
				a_star_alg.a_star_algorithm(utils.manhattan_heuristic)
				end = time.time()

				times.append(end - start)
				memory.append(a_star_alg.get_memory_usage())

			for t in times:
				file.write(str(t) + ',')
				average_time +=  t
			file.write(str(average_time/10) + '\n' + ' ,')
			for m in memory:
				file.write(str(m) + ',')
				average_memory += m
			file.write(str(average_memory/10) + '\n')

generate_boards2()
test_a_star2()
#test_a_star2() RODOU
#test_a_star1()
#test_dfs() RODOU
#test_idfs()
#test_bfs()