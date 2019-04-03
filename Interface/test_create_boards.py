# -*- coding: utf-8 -*-
import constants as c
import time
import shuffle
import bfs
import dfs
import it_dfs
import a_star
import utils
import numpy as np
import copy

shuffler = shuffle.Shuffle(3)
boards = []
num_shuffle = 1
for i in range(4):
    while len(boards) < 29:

        shuffler.shuffle_algorithm(num_shuffle)
        num_shuffle += 1

        astar_alg = a_star.A_STAR(shuffler.get_matrix(), 3)
        astar_alg.a_star_algorithm(utils.manhattan_heuristic)    

        move_list = astar_alg.get_solution_path()

        tam = len(move_list)

        if len(boards) == 0:
            tupla = (tam, shuffler.get_matrix())
            boards.append(tupla)     
        else:
            if not tam in (item[0] for item in boards):
                #print(shuffler.get_matrix())
                tupla = (tam, copy.copy(shuffler.get_matrix()))
                #print("TUPLA")
                #print(tupla)
                boards.append(tupla)
        #print("NUM SHUFFLE: " + str(num_shuffle))
        #print(len(boards))

    boards.sort()
    for board in boards:
        print(board[1])
    print 