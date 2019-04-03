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

def generate_boards2():
	for i in range(len(shuffle_number)):
		for j in range(test_number):
			shuffler = shuffle.Shuffle(board_size)
			shuffler.shuffle_algorithm(shuffle_number[i])
			boards[i][j] = shuffler.get_matrix()
def test_bfs():
	with open('/home/douglascorrea/FIA/BFS.csv', 'wb') as file:
		for i in range(len(shuffle_number)):
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			print("Moves: " + str(shuffle_number[i]))
			file.write(str(shuffle_number[i]) + '\n')
			for j in range(test_number):
				print(j)
				print(boards[i][j])
				bfs_alg = bfs.BFS(boards[i][j], board_size)

				start = time.time()
				bfs_alg.BFS_algorithm()
				end = time.time()

				times.append(end - start)
				memory.append(bfs_alg.get_memory_usage())

			file.write(' ' + ',')
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
		for i in range(len(shuffle_number)):
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			print("Moves: " + str(shuffle_number[i]))
			file.write(str(shuffle_number[i]) + '\n')
			for j in range(test_number):
				print(j)
				print(boards[i][j])
				dfs_alg = dfs.DFS(boards[i][j], board_size)

				start = time.time()
				dfs_alg.DFS_algorithm()
				end = time.time()

				times.append(end - start)
				memory.append(dfs_alg.get_memory_usage())

			file.write(' ' + ',')
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
		for i in range(len(shuffle_number)):
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			print("Moves: " + str(shuffle_number[i]))
			file.write(str(shuffle_number[i]) + '\n')
			for j in range(test_number):
				print(j)
				print(boards[i][j])
				dfs_it_alg = it_dfs.IT_DFS(boards[i][j], board_size)
				start = time.time()
				dfs_it_alg.IT_DFS_algorithm()
				end = time.time()

				times.append(end - start)
				memory.append(dfs_it_alg.get_memory_usage())
			file.write(' ' + ',')
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
		for i in range(len(shuffle_number)):
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			print("Moves: " + str(shuffle_number[i]))
			file.write(str(shuffle_number[i]) + '\n')
			for j in range(test_number):
				print(j)
				print(boards[i][j])
				a_star_alg = a_star.A_STAR(boards[i][j], board_size)
				start = time.time()
				a_star_alg.a_star_algorithm(utils.chessboard_heuristic)
				end = time.time()

				times.append(end - start)
				memory.append(a_star_alg.get_memory_usage())
			file.write(' ' + ',')
			for t in times:
				file.write(str(t) + ',')
				average_time +=  t
			file.write(str(average_time/10) + '\n' + ' ,')
			for m in memory:
				file.write(str(m) + ',')
				average_memory += m
			file.write(str(average_memory/10) + '\n')
def test_a_star2():
	with open('/home/douglascorrea/FIA/a_star2.csv', 'wb') as file:
		for i in range(len(shuffle_number)):
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			print("Moves: " + str(shuffle_number[i]))
			file.write(str(shuffle_number[i]) + '\n')
			for j in range(test_number):
				print(j)
				print(boards[i][j])
				a_star_alg = a_star.A_STAR(boards[i][j], board_size)
				start = time.time()
				a_star_alg.a_star_algorithm(utils.manhattan_heuristic)
				end = time.time()

				times.append(end - start)
				memory.append(a_star_alg.get_memory_usage())
			file.write(' ' + ',')
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
test_a_star1()
test_dfs()
test_idfs()
test_bfs()