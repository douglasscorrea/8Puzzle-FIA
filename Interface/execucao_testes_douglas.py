import time
import shuffle
import bfs
import dfs
import it_dfs
import a_star
import utils

board_size = 3
test_number = 10
shuffle_number = [10, 50, 100, 250, 500, 1000]
shuffler = shuffle.Shuffle(board_size)

def test_bfs():
	with open('/Users/douglascorrea/FIA/BFS.csv', 'wb') as file:
		for moves_number in shuffle_number:
			file.write(str(moves_number) + '\n')
			file.write(' ' + ',')
			print("Moves Number: " + str(moves_number))
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			for i in range (0, test_number):
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
	with open('/Users/douglascorrea/FIA/DFS.csv', 'wb') as file:
		for moves_number in shuffle_number:
			file.write(str(moves_number) + '\n')
			file.write(' ' + ',')
			print("Moves Number: " + str(moves_number))
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			for i in range (0, test_number):
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
	with open('/Users/douglascorrea/FIA/iDFS.csv', 'wb') as file:
		for moves_number in shuffle_number:
			file.write(str(moves_number) + '\n')
			file.write(' ' + ',')
			print("Moves Number: " + str(moves_number))
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			for i in range (0, test_number):
				shuffler.shuffle_algorithm(moves_number)
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
	with open('/Users/douglascorrea/FIA/a_star1.csv', 'wb') as file:
		for moves_number in shuffle_number:
			file.write(str(moves_number) + '\n')
			file.write(' ' + ',')
			print("Moves Number: " + str(moves_number))
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			for i in range (0, test_number):
				shuffler.shuffle_algorithm(moves_number)
				a_star_alg = a_star.A_STAR(shuffler.get_matrix(), board_size)

				start = time.time()
				a_star_alg.a_star_algorithm(utils.diff_heuristic)
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
	with open('/Users/douglascorrea/FIA/a_star2.csv', 'wb') as file:
		for moves_number in shuffle_number:
			file.write(str(moves_number) + '\n')
			file.write(' ' + ',')
			print("Moves Number: " + str(moves_number))
			times = []
			memory = []
			average_time = 0
			average_memory = 0
			for i in range (0, test_number):
				shuffler.shuffle_algorithm(moves_number)
				a_star_alg = a_star.A_STAR(shuffler.get_matrix(), board_size)

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

test_bfs()
#test_dfs()
#test_idfs()
#test_a_star1()
#test_a_star2()

