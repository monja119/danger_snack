import pygame as pygame

width = 500
height = 400


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Danger Snake')
