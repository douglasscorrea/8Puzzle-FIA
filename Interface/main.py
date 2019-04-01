# -*- coding: utf-8 -*-
import pygame, os, sys
import pygame_functions as pyf
import constants as c
import time
import shuffle
import bfs
import dfs
import it_dfs
import a_star
import utils

class Game_Interface:
    def __init__(self, nmax, filename):
        # Variaveis de Controle
        self.nmax = nmax
        self.mouse_state_plus = False
        self.mouse_state_minus = False
        #self.alg
        self.sprite_list = []
        self.shuffler = shuffle.Shuffle(self.nmax)
        self.imagesize = c.IMAGE_SIZE
        self.time_elapsed = 0

        # Inicializacao Pygame
        pyf.screenSize(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
        pyf.setBackgroundColour(c.GRAY)

        # Instancia lista de sprites
        for i in range (0, nmax*nmax):
            self.sprite_list.append(pyf.makeSprite("images/" + filename + str(i) + ".png"))

        # Carrega sprites padroes
        self.plus = pyf.makeSprite("images/plus.png")
        self.minus = pyf.makeSprite("images/minus.png")
        self.shuffle_button = pyf.makeSprite("images/shuffle.png")
        self.BFS_button = pyf.makeSprite("images/BFS.png")
        self.DFS_button = pyf.makeSprite("images/DFS.png")
        self.DFS_IT_button = pyf.makeSprite("images/BFS_IT.png")
        self.A1_button = pyf.makeSprite("images/A_H1.png")
        self.A2_button = pyf.makeSprite("images/A_H2.png")
        self.text_shuffler_label = pyf.makeLabel(u"Número de iterações: ", 30, 50, 690, "black", "Arial", "clear")
        self.text_time = pyf.makeLabel(u"Tempo de execução: ", 30, 700, 400, "black", "Arial", "clear")
        self.text_time2 = pyf.makeLabel("segundos", 30, 980, 400, "black", "Arial", "gray")
        self.text_memory = pyf.makeLabel(u"Memória utilizada: ", 30, 735, 450, "black", "Arial", "clear")
        #self.text_moves = pyf.makeLabel("Movimentos Realizados: ", 30, 735, 500, "black", "Arial", "clear")
        #self.text_moves2 = pyf.makeLabel("", 30, 735, 500, "black", "Arial", "gray")
        self.text_memory2 = pyf.makeLabel("bytes", 30, 980, 450, "black", "Arial", "gray")
        self.number_shuffler_label = pyf.makeLabel(str(c.IT), 30, 332, 692, "black", "Arial", "clear")

        # Transforma sprites para tamanhos maiores que 3x3
        if self.nmax > 3:
            self.initial_transformation()

        # Posiciona Sprites
        self.initial_position()
        pyf.moveSprite(self.shuffle_button, 570, 710, True)
        pyf.moveSprite(self.plus, 515, 710, True)
        pyf.moveSprite(self.minus, 460, 710, True)
        pyf.moveSprite(self.BFS_button, 800, 100, True)
        pyf.moveSprite(self.DFS_button, 1010, 100, True)
        pyf.moveSprite(self.DFS_IT_button, 900, 210, True)
        pyf.moveSprite(self.A1_button, 800, 320, True)
        pyf.moveSprite(self.A2_button, 1010, 320, True)

        # Mostra sprites na tela
        for i in range(0, nmax*nmax):
            pyf.showSprite(self.sprite_list[i])
            # print(i)
        pyf.showSprite(self.shuffle_button)
        pyf.showSprite(self.plus)
        pyf.showSprite(self.minus)
        pyf.showLabel(self.text_shuffler_label)
        pyf.showLabel(self.number_shuffler_label)
        pyf.showLabel(self.BFS_button)
        pyf.showLabel(self.DFS_button)
        pyf.showLabel(self.DFS_IT_button)
        pyf.showLabel(self.A1_button)
        pyf.showLabel(self.A2_button)
        pyf.showLabel(self.text_time)
        pyf.showLabel(self.text_time2)
        pyf.showLabel(self.text_memory)
        pyf.showLabel(self.text_memory2)
        #pyf.showLabel(self.text_moves)
        #pyf.showLabel(self.text_moves2)
        pyf.transformSprite(self.shuffle_button, 0, 0.25)
        pyf.transformSprite(self.plus, 0, 0.25)
        pyf.transformSprite(self.minus, 0, 0.1)


    def initial_position(self):
        ini_pos = self.imagesize/2 + c.SPRITE_BORDER
        count_index = 1
        for i in range (0, self.nmax):
            for j in range(0, self.nmax):
                pyf.moveSprite(self.sprite_list[count_index], ini_pos + (j * self.imagesize), ini_pos + (i * self.imagesize), True)
                count_index += 1
                if count_index == self.nmax*self.nmax:
                    break

        pyf.moveSprite(self.sprite_list[0], ini_pos + ((self.nmax - 1) * self.imagesize), ini_pos + ((self.nmax - 1) * self.imagesize), True)


    def initial_transformation(self):
        factor = (600.0/self.nmax) / self.imagesize
        self.imagesize = self.imagesize * factor
        for i in range(0, self.nmax * self.nmax):
            pyf.transformSprite(self.sprite_list[i], 0, factor)


    def run(self):
        # RODA ATE A TECLA ESC SER PRESSIONADA
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        waittime = 0
        while not keys[pygame.K_ESCAPE]:
            current_time = pygame.time.get_ticks()
            if current_time > waittime:
                pygame.event.clear()
                keys = pygame.key.get_pressed()
                waittime += 20

            # Incrementa Iteracoes
            if pyf.spriteClicked(self.plus):
                if not self.mouse_state_plus:
                    self.mouse_state_plus = True
                    if c.IT >= 1000:
                        c.IT += 1000
                    elif c.IT >= 100:
                        c.IT += 100
                    elif c.IT >= 10:
                        c.IT += 10
                    else:
                        c.IT += 1
                pyf.changeLabel(self.number_shuffler_label, str(c.IT))
            else:
                self.mouse_state_plus = False
            # Decrementa Iteracoes
            if pyf.spriteClicked(self.minus):
                if not self.mouse_state_minus:
                    self.mouse_state_minus = True
                    if c.IT > 1000:
                        c.IT -= 1000
                    elif c.IT > 100:
                        c.IT -= 100
                    elif c.IT > 10:
                        c.IT -= 10
                    elif c.IT > 0:
                        c.IT -= 1
                pyf.changeLabel(self.number_shuffler_label, str(c.IT))
            else:
                self.mouse_state_minus = False
            # Botao Shuffle
            if pyf.spriteClicked(self.shuffle_button): # ao clicar o sprite do shuffler chama o metodo para embaralhar
                self.initial_position()
                self.shuffler_method(c.IT)

            # Botoes Algoritmos
            move_list = []

            # BFS
            if pyf.spriteClicked(self.BFS_button):
                bfs_alg = bfs.BFS(self.shuffler.get_matrix(), self.nmax)
                start = time.time()
                bfs_alg.BFS_algorithm()
                end = time.time()

                if end - start < 1:
                    pyf.changeLabel(self.text_time2, "{0:.3f}".format((end - start) * 1000) + "ms")
                else:
                    pyf.changeLabel(self.text_time2, "{0:.3f}".format(end - start) + "s")

                pyf.changeLabel(self.text_memory2, "{0:.3f}".format(bfs_alg.get_memory_usage()) + "MB")
                move_list = bfs_alg.get_solution_path()
                self.move_numbers(move_list, True)
                self.shuffler.reset_matrix()


            # DFS
            if pyf.spriteClicked(self.DFS_button):
                dfs_alg = dfs.DFS(self.shuffler.get_matrix(), self.nmax)
                start = time.time()
                dfs_alg.DFS_algorithm()
                end = time.time()

                if end - start < 1:
                    pyf.changeLabel(self.text_time2, "{0:.3f}".format((end - start) * 1000) + "ms")
                else:
                    pyf.changeLabel(self.text_time2, "{0:.3f}".format(end - start) + "s")

                pyf.changeLabel(self.text_memory2, "{0:.0f}".format(dfs_alg.get_memory_usage()) + "bytes")
                move_list = dfs_alg.get_solution_path()
                self.move_numbers(move_list, True)
                self.shuffler.reset_matrix()

            # DFS_IT
            if pyf.spriteClicked(self.DFS_IT_button):
                # modificar manualmente a profundidade máxima inicial
                dfs_it_alg = it_dfs.IT_DFS(self.shuffler.get_matrix(), self.nmax)
                start = time.time()
                dfs_it_alg.IT_DFS_algorithm()
                end = time.time()

                if end - start < 1:
                    pyf.changeLabel(self.text_time2, "{0:.3f}".format((end - start) * 1000) + "ms")
                else:
                    pyf.changeLabel(self.text_time2, "{0:.3f}".format(end - start) + "s")

                pyf.changeLabel(self.text_memory2, "{0:.0f}".format(dfs_it_alg.get_memory_usage()) + "bytes")
                move_list = dfs_it_alg.get_solution_path()
                self.move_numbers(move_list, True)
                self.shuffler.reset_matrix()

            # A_STAR H1
            if pyf.spriteClicked(self.A1_button):
                astar_alg = a_star.A_STAR(self.shuffler.get_matrix(), self.nmax)
                start = time.time()
                astar_alg.a_star_algorithm(utils.diff_heuristic)
                end = time.time()

                if end - start < 1:
                    pyf.changeLabel(self.text_time2, "{0:.3f}".format((end - start) * 1000) + "ms")
                else:
                    pyf.changeLabel(self.text_time2, "{0:.3f}".format(end - start) + "s")

                pyf.changeLabel(self.text_memory2, "{0:.0f}".format(astar_alg.get_memory_usage()) + "bytes")
                move_list = astar_alg.get_solution_path()
                self.move_numbers(move_list, True)
                self.shuffler.reset_matrix()

            # A_STAR H2
            if pyf.spriteClicked(self.A2_button):
                astar_alg = a_star.A_STAR(self.shuffler.get_matrix(), self.nmax)
                start = time.time()
                astar_alg.a_star_algorithm(utils.manhattan_heuristic)
                end = time.time()

                if end - start < 1:
                    pyf.changeLabel(self.text_time2, "{0:.3f}".format((end - start) * 1000) + "ms")
                else:
                    pyf.changeLabel(self.text_time2, "{0:.3f}".format(end - start) + "s")

                pyf.changeLabel(self.text_memory2, "{0:.0f}".format(astar_alg.get_memory_usage()) + "bytes")
                move_list = astar_alg.get_solution_path()
                self.move_numbers(move_list, True)
                self.shuffler.reset_matrix()

        pyf.endWait()

    def shuffler_method(self, n_moves):
        self.shuffler.shuffle_algorithm(n_moves)
        moves_list = self.shuffler.get_moves_list()
        self.move_numbers(moves_list, False)

    def change_position(self, m, flag): #m=n?
        pos_correction = self.imagesize/2
        n0_x, n0_y = self.sprite_list[0].getPosition()  # X e Y do zero
        x_pos, y_pos = self.sprite_list[m].getPosition()  # X e Y da posicao que sera trocada com 0
        x_temp, y_temp = self.sprite_list[m].getPosition()  # Temporario
        n0_y += pos_correction
        n0_x += pos_correction
        y_temp = y_temp+pos_correction
        x_temp = x_temp+pos_correction
        y_pos += pos_correction
        x_pos += pos_correction

        pyf.moveSprite(self.sprite_list[0], x_pos, y_pos, True) # muda posição do 0
        if flag:
            if n0_y > y_temp:
                for x in range(0, int(self.imagesize/5)):
                    y_pos += 5
                    pyf.moveSprite(self.sprite_list[m], x_pos, y_pos, True)
                    if flag:
                         time.sleep(c.TIME_CONST)
            elif n0_y < y_temp:
                for x in range(0, int(self.imagesize/5)):
                    y_pos -= 5
                    pyf.moveSprite(self.sprite_list[m], x_pos, y_pos, True)
                    if flag:
                        time.sleep(c.TIME_CONST)
            elif n0_x > x_temp:
                for x in range(0, int(self.imagesize/5)):
                    x_pos += 5
                    pyf.moveSprite(self.sprite_list[m], x_pos, y_pos, True)
                    if flag:
                        time.sleep(c.TIME_CONST)
            elif n0_x < x_temp:
                for x in range(0, int(self.imagesize/5)):
                    x_pos -= 5
                    pyf.moveSprite(self.sprite_list[m], x_pos, y_pos, True)
                    if flag:
                        time.sleep(c.TIME_CONST)
        else:
            if n0_y > y_temp:
                pyf.moveSprite(self.sprite_list[m], x_pos, y_pos + self.imagesize, True)
            elif n0_y < y_temp:
                pyf.moveSprite(self.sprite_list[m], x_pos, y_pos - self.imagesize, True)
            elif n0_x > x_temp:
                pyf.moveSprite(self.sprite_list[m], x_pos + self.imagesize, y_pos, True)
            else:
                pyf.moveSprite(self.sprite_list[m], x_pos - self.imagesize, y_pos, True)


    def move_numbers(self, moves, flag):
        for move in moves:
            self.change_position(move, flag)

    def text_objects(self, text, font, color_text):
        text_surface = font.render(text, True, color_text)
        return text_surface, text_surface.get_rect()



#game = Game_Interface(5, c.FILENAME_STD)
game = Game_Interface(3, c.FILENAME_MAT)

game.run()