''' TODO:

Make creeps travel with A* algorithm

'''

import pygame
import math
import random
from creeps import Creep
from towers import Tower, Bullet
pygame.init()

size = width, height = 700, 900
screen = pygame.display.set_mode((size))
running = 1

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0

time = 0


tower1 = Tower(screen, red, 100, 100, 25, 25, width, height)
tower2 = Tower(screen, red, 600, 600, 25, 25, width, height)
towers = [tower1, tower2]
creeps = []
clock = pygame.time.Clock()

while running:
    while len(creeps) < 5:
        creep = Creep(screen, blue, (0, random.randint(0,height)), (0, 350))
        creeps.append(creep)
    clock.tick(60)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 3:
            tower1.shoot(pygame.mouse.get_pos(), "homing")
            tower2.shoot(pygame.mouse.get_pos(), "homing")
        else:
            tower1.shoot(pygame.mouse.get_pos(), "null")
            tower2.shoot(pygame.mouse.get_pos(), "null")

    screen.fill((black))
    for creep in creeps:
        creep.updatePosition()
        creep.drawCreep(screen)

    for tower in towers:
        tower.update(creeps)
        for bullet in tower.bullets:
            for creep in creeps:
                if bullet.rect.colliderect(creep.rect):
                    creep.attacked(25)
                    if creep.health < 1:
                        creeps.remove(creep)
                    try:
                        tower.bullets.remove(bullet)
                    except:
                        print "eh"

    pygame.display.flip()
    time += 1
