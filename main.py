"""
    /* -----------------------------------------------
    /* Author : MONJA  - monja.sesame@gmail.com
    /* GitHub : github.com/monja119/danger_snake
    /* How to use? : Check the GitHub README
    /* v1.0.0
    /* ----------------------------------------------- */

"""

import pygame
from random import *
from pygame.locals import *
from game import Game, width, height
import body
import sys

pygame.init()

clock = pygame.time.Clock()
text = pygame.font.SysFont('Georgia', 15)
msg = text.render('Game Over ! (Enter)', True, 'red')


class Run:
    def __init__(self):
        self.player_rect = ''
        self.player_surface = ''
        self.player_new = ''
        self.apple_pos = (0, 0)
        self.snake_pos = (0, 0)
        self.apple_rect = ''
        self.apple_y = 0
        self.apple_x = 0
        self.running = True
        self.bg = Game()
        self.body = body.Body
        # snake
        self.snake_pos0 = (250, 200)
        self.apple_size = (10, 10)
        self.speed = 10
        self.moves = 0
        self.x, self.y = self.snake_pos0[0], self.snake_pos0[1]

        self.snake_body = [(self.x, self.y)]
        self.move()

        # apple
        self.apple()
        self.apple_color = 'red'
        self.apple_surface = pygame.Surface((10, 10))
        self.apple_surface.fill(self.apple_color)

        # running
        self.status = 'ready'
        self.step = 3
        self.catch = 0
        self.level = 1

    def text(self, font, size, color, value, x, y):
        my_text = pygame.font.SysFont(font, size)
        text_render = my_text.render(value, True, color)
        self.bg.window.blit(text_render, (x, y))

    def load_body(self, x, y):
        self.bg.window.blit(self.body(x, y).surface, self.body(x, y).rect)

    def apple(self):
        self.apple_x = choice(range(0, 390, 10))
        while self.apple_x in self.snake_body:
            self.apple_x = choice(range(0, 390, 10))

        self.apple_y = choice(range(30, 390, 10))
        while self.apple_y in self.snake_body:
            self.apple_y = choice(range(30, 390, 10))

    def load_apple(self):
        self.apple_rect = pygame.Rect((self.apple_x, self.apple_y), self.apple_size)
        self.bg.window.blit(self.apple_surface, self.apple_rect)

    def move(self):
        self.body(self.x, self.y)

    def catching(self):
        self.snake_pos = (self.x, self.y)
        self.apple_pos = (self.apple_x, self.apple_y)
        if self.apple_pos == self.snake_pos:
            self.catch += 1
            self.level += 1
            self.snake_body.append(self.snake_pos)
            self.apple()
            self.load_apple()
            print("catching : ", self.catch)

    def game_over(self):
        last = self.snake_body[:-1]
        if self.x >= width or self.x < 0 or self.y >= height or self.y < 0 or (self.x, self.y) in last and self.status != 'stop':
            self.status = 'stop'
            app.text('Joker Man', 25, 'red', 'Game Over !', (width / 2) - 70, (height / 2)-20)
            pygame.display.flip()

    def set_level(self, x):
        x = self.step + self.catch + 1
        self.level = x

    def initial(self):
        self.x, self.y = self.snake_pos0[0], self.snake_pos0[1]
        self.snake_body = [(self.x, self.y)]
        self.level = 3
        self.catch = 0
        self.status = 'running'
        self.moves = 0
        self.apple()
        self.load_apple()
        self.move()
        self.load_game()

    def load_game(self):
        if running and self.status == 'running':
            self.bg.window.fill('black')

            # affichage de la pomme
            self.load_apple()

            # affichage du serpent
            for i in range(len(self.snake_body)):
                if i == len(self.snake_body) - 1:
                    head = self.body(self.snake_body[i][0], self.snake_body[i][1]).surface
                    head.fill('green')
                    self.bg.window.blit(head, self.body(self.snake_body[i][0], self.snake_body[i][1]).rect)
                else:
                    x = self.snake_body[i][0]
                    y = self.snake_body[i][1]
                    self.load_body(x, y)
            self.set_level(self.catch)

            self.text('Joker man', 15, 'white', str(self.catch), (width / 2) - 15, 10)
            self.text('monospace', 10, 'white', 'MONJA@2022', width - 7 - 60, height - 10)
            pygame.display.flip()


app = Run()
running = True
traject = 0
while running:
    # timing

    clock.tick(app.level)
    app.moves += 1
    # guiding
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            # gestion de status
            if app.status == 'ready':
                app.status = 'running'
            if app.status == 'stop':
                app.initial()

            # gestion de touches
            if event.key == K_DOWN and traject != 0:
                app.speed = abs(app.speed)
                traject = 0
            if event.key == K_UP and traject != 0:
                app.speed = -abs(app.speed)
                traject = 0
            if event.key == K_RIGHT and traject != 1:
                app.speed = abs(app.speed)
                traject = 1
            if event.key == K_LEFT and traject != 1:
                app.speed = -abs(app.speed)
                traject = 1
            if event.key == K_SPACE:
                if app.status == 'pause':
                    app.status = 'running'
                else:
                    app.status = 'pause'
            if event.key == K_ESCAPE:
                running = False
                app.text('Times New Romain', 25, 'white', 'Thank you', (width / 2) - 40, (height / 2) - 100)
                pygame.display.flip()
                pygame.time.wait(2000)
                pygame.quit()

    # Homepage
    if app.status == 'ready':
        app.bg.window.fill('black')
        first = pygame.Surface((10, 10))
        first.fill('green')
        app.bg.window.blit(first, pygame.Rect((width / 2 - 27, height / 2 - 10), (10, 10)))

        # instructions
        app.text('Joker man', 55, 'green', 'Danger Snack', 50, 50)
        app.text('Joker man', 25, 'red', 'Ready ?', (width / 2) - 60, (height / 2))
        app.text('monospace', 13, 'white', '(Press Any Key)', (width / 2) - 70, (height / 2) + 50)
        app.text('Times New Roman', 13, 'white', 'Mouvement : key up, down, right and right', 10, (height / 2) + 100)
        app.text('Times New Roman', 13, 'white', 'Pause : Space', 10, (height / 2) + 115)
        app.text('Times New Roman', 13, 'white', 'Quit : Escape', 10, (height / 2) + 130)

        # contact
        app.text('Times New Roman', 13, 'white', 'monja.sesame@gmail.com', 10, height - 20)
        app.text('Times New Roman', 13, 'white', 'https://github.com/monja119', 190, height - 20)
        app.text('Times New Roman', 13, 'white', '+261 34 08 612 63', 390, height - 20)
        pygame.display.flip()
    elif app.status == 'pause' or app.status == 'stop':
        pass
    else:
        # multiplying
        snake_tail = app.snake_body[0]

        if traject == 0:
            app.y += app.speed
        else:
            app.x += app.speed
        app.catching()
        app.game_over()
        if app.status != 0:
            for k in range(len(app.snake_body) - 1):
                app.snake_body[k] = app.snake_body[k + 1]
            app.snake_body[len(app.snake_body) - 1] = (app.x, app.y)
            app.move()
            app.load_game()
