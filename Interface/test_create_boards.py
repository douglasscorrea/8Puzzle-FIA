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
import operator
def executa_BFS(board, tam):
    with open('BFS.csv', 'a') as file:
        counter = 1
        print(board)
        file.write(str(tam) + '\n')
        bfs_alg = bfs.BFS(board,3)
        start = time.time()
        bfs_alg.BFS_algorithm()
        end = time.time()

        times = end - start 
        file.write(str(times) + ',')
        file.write(str(bfs_alg.get_memory_usage()) + ',')
        file.write('\n')

# def executa_DFS(boards):

# def executa_DFSIT(boards):

# def executa_ASTAR1(boards):

# def executa_ASTAR2(boards):

def create_Boards(size):
    shuffler = shuffle.Shuffle(size)
    boards = []
    num_shuffle = 1
    while len(boards) < 25:

        shuffler.shuffle_algorithm(num_shuffle)
        num_shuffle += 1

        astar_alg = a_star.A_STAR(shuffler.get_matrix(), 3)
        astar_alg.a_star_algorithm(utils.manhattan_heuristic)    

        move_list = astar_alg.get_solution_path()

        tam = len(move_list)

        if len(boards) == 0:
            tupla = (tam, copy.copy(shuffler.get_matrix()))
            print("ENtrou")
            print(tupla)
            boards.append(copy.copy(tupla))     
        else:
            if not tam in (item[0] for item in boards) and tam != 0 :
                tupla = (tam, copy.copy(shuffler.get_matrix()))
                print(tupla)
                boards.append(copy.copy(tupla))

    boards.sort(key = operator.itemgetter(0))

    print(boards)
    # tabuleiros = []
    # for board in boards:
    #     tabuleiros.append(copy.copy(board[1]))

    return boards


boards = create_Boards(3)

for board in boards:
    print("Profundidade do board: " + str(board[0]))
    executa_BFS(board[1], board[0])

