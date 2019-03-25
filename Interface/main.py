import pygame, os, sys
from pygame.locals import *
import pygame_functions as pyf
import constants as c
import time
import controls as co
import shuffle



class Game_Interface:
    def __init__(self):
        pyf.screenSize(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
        pyf.setBackgroundColour(c.GRAY)
        n0 = pyf.makeSprite("/home/paulohenrik/GIT-repository/8Puzzle-FIA/Interface/images/0.png")
        n1 = pyf.makeSprite("/home/paulohenrik/GIT-repository/8Puzzle-FIA/Interface/images/1.png")
        n2 = pyf.makeSprite("/home/paulohenrik/GIT-repository/8Puzzle-FIA/Interface/images/2.png")
        n3 = pyf.makeSprite("/home/paulohenrik/GIT-repository/8Puzzle-FIA/Interface/images/3.png")
        n4 = pyf.makeSprite("/home/paulohenrik/GIT-repository/8Puzzle-FIA/Interface/images/4.png")
        n5 = pyf.makeSprite("/home/paulohenrik/GIT-repository/8Puzzle-FIA/Interface/images/5.png")
        n6 = pyf.makeSprite("/home/paulohenrik/GIT-repository/8Puzzle-FIA/Interface/images/6.png")
        n7 = pyf.makeSprite("/home/paulohenrik/GIT-repository/8Puzzle-FIA/Interface/images/7.png")
        n8 = pyf.makeSprite("/home/paulohenrik/GIT-repository/8Puzzle-FIA/Interface/images/8.png")

        self.spriteList = [n0, n1,n2,n3,n4,n5,n6,n7,n8]

        pyf.moveSprite(self.spriteList[1], 150, 150, True)
        pyf.moveSprite(self.spriteList[2], 350, 150, True)
        pyf.moveSprite(self.spriteList[3], 550, 150, True)
        pyf.moveSprite(self.spriteList[4], 150, 350, True)
        pyf.moveSprite(self.spriteList[5], 350, 350, True)
        pyf.moveSprite(self.spriteList[6], 550, 350, True)
        pyf.moveSprite(self.spriteList[7], 150, 550, True)
        pyf.moveSprite(self.spriteList[8], 350, 550, True)
        pyf.moveSprite(self.spriteList[0], 550, 550, True)

        #pyf.transformSprite(n2, 0, 0.88)  Usar para tabuleiro maior que 3x3

        pyf.showSprite(self.spriteList[0])
        pyf.showSprite(self.spriteList[1])
        pyf.showSprite(self.spriteList[2])
        pyf.showSprite(self.spriteList[3])
        pyf.showSprite(self.spriteList[4])
        pyf.showSprite(self.spriteList[5])
        pyf.showSprite(self.spriteList[6])
        pyf.showSprite(self.spriteList[7])
        pyf.showSprite(self.spriteList[8])

        self.shuffler = shuffle.Shuffle()
        self.shuffler.shuffle_algorithm(1000)
        moves_list = self.shuffler.get_moves_list()
        print(moves_list)
        self.movementTest(moves_list)

        pyf.endWait()

    def change_position(self, m): #m=n?
        n0_x, n0_y = self.spriteList[0].getPosition()
        x_pos, y_pos = self.spriteList[m].getPosition()
        x_temp, y_temp = self.spriteList[m].getPosition()
        n0_y += 100
        n0_x += 100
        y_temp = y_temp+100
        x_temp = x_temp+100
        y_pos += 100
        x_pos += 100

        pyf.moveSprite(self.spriteList[0], x_pos, y_pos, True) # muda posição do 0

        if n0_y > y_temp:
            for x in range(0, 50):
                y_pos += 4
                pyf.moveSprite(self.spriteList[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)
        elif n0_y < y_temp:
            for x in range(0, 50):
                y_pos -= 4
                pyf.moveSprite(self.spriteList[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)
        elif n0_x > x_temp:
            for x in range(0, 50):
                x_pos += 4
                pyf.moveSprite(self.spriteList[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)
        elif n0_x < x_temp:
            for x in range(0, 50):
                x_pos -= 4
                pyf.moveSprite(self.spriteList[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)

    def movementTest(self, moves):
        for move in moves:
            self.change_position(move)

game = Game_Interface()