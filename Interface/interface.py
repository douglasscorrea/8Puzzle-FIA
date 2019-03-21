import pygame, os, sys
from pygame.locals import *
import constants as c
import controls as co


os.environ['SDL_VIDEO_CENTERED'] = '1'


class Game_Interface:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(c.SCREEN_SIZE)
        pygame.display.set_caption(c.TITLE)
       # for i in range (0,)
        self.button('', 24, c.CONTOUR_MENU, 100, 100, 600, 600, c.BLUE, c.BLUE_B)

    def text_objects(self, text, font, color_text):
        text_surface = font.render(text, True, color_text)
        return text_surface, text_surface.get_rect()

    def button(self, msg, fs, bd, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        line = bd
        pygame.draw.rect(self.display, c.BLACK, (x - (line / 2), y - (line / 2), w + line, h + line))
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.display, ac, (x, y, w, h))
            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(self.display, ic, (x, y, w, h))
        small_text = pygame.font.Font(c.FONT_1, fs)
        text_surf, text_rect = self.text_objects(msg, small_text, c.BLACK)
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        self.display.blit(text_surf, text_rect)

    def quit(self):
        pygame.quit()
        sys.exit()

    def board(self):
        self.button('BFS', 24, c.CONTOUR_MENU, c.SCREEN_WIDTH - 300, 50, 100, 60, c.BLUE, c.BLUE_B)
        self.button('DFS', 24, c.CONTOUR_MENU, c.SCREEN_WIDTH - 150, 50, 100, 60, c.BLUE, c.BLUE_B)
        self.button('It DFS', 24, c.CONTOUR_MENU, c.SCREEN_WIDTH - 300, 160, 100, 60, c.BLUE, c.BLUE_B)
        self.button('A* H1', 24, c.CONTOUR_MENU, c.SCREEN_WIDTH - 150, 160, 100, 60, c.BLUE, c.BLUE_B)
        self.button('A* H2', 24, c.CONTOUR_MENU, c.SCREEN_WIDTH - 225, 270, 100, 60, c.BLUE, c.BLUE_B)


def init_game():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                interface.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    interface.quit()

        interface.board()

        clock.tick(c.FPS)
        pygame.display.update()


interface = Game_Interface()
clock = pygame.time.Clock()
init_game()
