import pygame


class Body:
    def __init__(self, x, y):
        # proprieties de snack
        self.color = 'yellow'
        self.size = (10, 10)
        self.speed = 0
        self.speed_x, self.speed_y = 10, 10
        self.traject = 0
        self.surface = pygame.Surface((10, 10))
        self.surface.fill('yellow')

        # initial position
        self.x0, self.y0 = 250, 200
        # position a instant
        self.x, self.y = 0, 0

        # apple
        self.apple_color = 'red'
        self.apple_size = (10, 10)
        self.apple_surface = pygame.Surface((10, 10))
        self.apple_surface.fill(self.apple_color)

        self.rect = pygame.Rect((x, y), self.size)

    def set_speed(self, value):
        self.speed = 1.5
