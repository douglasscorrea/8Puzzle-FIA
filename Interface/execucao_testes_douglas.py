# -*- coding: utf-8 -*-

# import pygame, os, sys
# import pygame_functions as pyf
# import constants as c
import time
import shuffle
import bfs
import dfs
import it_dfs
import a_star
import utils
# import csv

test_number = 10
shuffle_number = [10, 50, 100, 250, 500, 1000]
shuffler = shuffle.Shuffle(3)

def test_a_star2():
	with open('/home/douglascorrea/FIA/a_star2.csv', 'wb') as file:
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
				a_star_alg = a_star.A_STAR(shuffler.get_matrix(), 3)

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

test_a_star2()

