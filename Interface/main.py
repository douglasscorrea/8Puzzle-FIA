import pygame, os, sys
import pygame_functions as pyf
import constants as c
import time
import shuffle


class Game_Interface:
    def __init__(self, nmax, filename):
        # Variaveis de Controle
        self.nmax = nmax
        self.mouse_state_plus = False
        self.mouse_state_minus = False
        self.sprite_list = []
        self.shuffler = shuffle.Shuffle(self.nmax)
        self.imagesize = c.IMAGE_SIZE

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
        self.BFS_IT_button = pyf.makeSprite("images/BFS_IT.png")
        self.BFS_IT_button = pyf.makeSprite("images/BFS_IT.png")
        self.A1_button = pyf.makeSprite("images/A_H1.png")
        self.A2_button = pyf.makeSprite("images/A_H2.png")
        self.text_shuffler_label = pyf.makeLabel("Numero de iteracoes: ", 30, 50, 690, "black", "Arial", "clear")
        self.number_shuffler_label = pyf.makeLabel(str(c.IT), 30, 332, 692, "black", "Arial", "clear")

        # Transforma sprites para tamanhos maiores que 3x3
        if self.nmax > 3:
            self.initial_transformation()

        # Posiciona Sprites
        self.initial_position()
        pyf.moveSprite(self.shuffle_button, 490, 710, True)
        pyf.moveSprite(self.plus, 400, 710, True)
        pyf.moveSprite(self.minus, 440, 710, True)
        pyf.moveSprite(self.BFS_button, 800, 100, True)
        pyf.moveSprite(self.DFS_button, 1010, 100, True)
        pyf.moveSprite(self.BFS_IT_button, 900, 210, True)
        pyf.moveSprite(self.A1_button, 800, 320, True)
        pyf.moveSprite(self.A2_button, 1010, 320, True)

        # Mostra sprites na tela
        for i in range(0, nmax*nmax):
            pyf.showSprite(self.sprite_list[i])
        pyf.showSprite(self.shuffle_button)
        pyf.showSprite(self.plus)
        pyf.showSprite(self.minus)
        pyf.showLabel(self.text_shuffler_label)
        pyf.showLabel(self.number_shuffler_label)
        pyf.showLabel(self.BFS_button)
        pyf.showLabel(self.DFS_button)
        pyf.showLabel(self.BFS_IT_button)
        pyf.showLabel(self.A1_button)
        pyf.showLabel(self.A2_button)
        pyf.transformSprite(self.shuffle_button, 0, 0.35)
        pyf.transformSprite(self.plus, 0, 0.25)
        pyf.transformSprite(self.minus, 0, 0.25)


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
        factor = (600/self.nmax) / self.imagesize
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

        pyf.endWait()

    def shuffler_method(self, n_moves):
        self.shuffler.shuffle_algorithm(n_moves)
        moves_list = self.shuffler.get_moves_list()
        self.move_numbers(moves_list)

    def change_position(self, m): #m=n?
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
        if n0_y > y_temp:
            for x in range(0, int(self.imagesize/5)):
                y_pos += 5
                pyf.moveSprite(self.sprite_list[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)
        elif n0_y < y_temp:
            for x in range(0, int(self.imagesize/5)):
                y_pos -= 5
                pyf.moveSprite(self.sprite_list[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)
        elif n0_x > x_temp:
            for x in range(0, int(self.imagesize/5)):
                x_pos += 5
                pyf.moveSprite(self.sprite_list[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)
        elif n0_x < x_temp:
            for x in range(0, int(self.imagesize/5)):
                x_pos -= 5
                pyf.moveSprite(self.sprite_list[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)

    def move_numbers(self, moves):
        for move in moves:
            self.change_position(move)

    def text_objects(self, text, font, color_text):
        text_surface = font.render(text, True, color_text)
        return text_surface, text_surface.get_rect()



game = Game_Interface(4, c.FILENAME_STD)
game.run()