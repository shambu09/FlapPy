#! python3

import pygame
from pygame.locals import *
from ResourcePath import resource_path
from Classes import Pipe
from Classes import Foot
from Classes import Flappy
import random

pygame.init()

bg = pygame.image.load(resource_path(r'Assets/bg.png'))
pipeU = pygame.image.load(resource_path(r'Assets/pipeU.png'))
pipeD = pygame.image.load(resource_path(r'Assets/pipeD.png'))
global flappyP
flappyP = [pygame.image.load(resource_path(r'Assets/FlappyB0.png')), pygame.image.load(
    resource_path(r'Assets/FlappyB1.png')), pygame.image.load(resource_path(r'Assets/FlappyB2.png'))]
foot = pygame.image.load(resource_path(r'Assets/Foot.png'))

bg = pygame.transform.scale2x(bg)
pipeD = pygame.transform.scale2x(pipeD)
for i in range(len(flappyP)):
    flappyP[i] = pygame.transform.scale2x(flappyP[i])
footP = pygame.transform.scale2x(foot)

width = 288
height = 512

canvas = width, height

clock = pygame.time.Clock()

win = pygame.display.set_mode(canvas)

pygame.display.set_caption('Flappy Bird')

pipes = []

foots = [Foot(0, footP), Foot(336, footP)]

Animation = 0

flappy = Flappy((height - 108) // 2, flappyP[0], flappyP)
pygame.time.set_timer(USEREVENT + 1, 2000)


def Draw(pipes, win, foots, flappy):
    win.blit(bg, (0, 0))

    if flappy.life:
        ALiveMovement(pipes, win, foots, flappy)
    else:
        for pipe in reversed(pipes):
            pipe.show(win)
        for foot in foots:
            foot.show(win)
    flappy.show(win)
    flappy.gravity()
    pygame.display.update()


def noCollision(pipes, bird):
    return pygame.Rect(bird).collidelist(pipes) == -1


def ALiveMovement(pipes, win, foots, flappy):
    T = []
    flappy.scoreArray = []
    for pipe in reversed(pipes):
        pipe.show(win)
        pipe.update()
        if pipe.OUT():
            pipes.remove(pipe)

    for pipe in pipes:
        T.append(pipe.rect1())
        T.append(pipe.rect2())
        flappy.scoreArray.append(pipe.score())

    Collision(win, flappy, T, foot)

    if flappy.rect().collidelist(flappy.scoreArray) != -1:
        flappy.score += 0.1

    if flappy.y >= 385:
        flappy.bird = pygame.transform.rotate(flappyP[0], -90)
        flappy.life = False
        win.fill((255, 255, 255))

    if flappy.y + 10 <= 0:
        flappy.y = 0


def Collision(win, flappy, T, foot):
    if noCollision(T, flappy.rect()):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            flappy.bird = flappy.imageU[int(Animation % 3)]
            flappy.Jump()
        else:
            flappy.bird = flappy.imageD[int(Animation % 3)]
    else:
        flappy.bird = pygame.transform.rotate(flappyP[0], -90)
        flappy.life = False
        win.fill((255, 255, 255))

    for foot in foots:
        foot.show(win)
        foot.update()
        if foot.OUT():
            foot.x = 336


run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT + 1:
            if flappy.life:
                pipes.append(Pipe(290, random.randrange(50, 280), pipeD))
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    Draw(pipes, win, foots, flappy)
    Animation += 0.3

pygame.quit()
quit()
