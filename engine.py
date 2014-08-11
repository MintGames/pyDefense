''' TODO:

Make creeps travel with A* algorithm

'''

import pygame
import math
import random
from creeps import CreepWave
from towers import Tower, Bullet
from path import Path
pygame.init()
import timeit

time = timeit.default_timer() 

size = width, height = 700, 900
screen = pygame.display.set_mode((size))
running = 1

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0

time = 0
currentWave = 1


tower1 = Tower(screen, red, 100, 100, 25, 25, width, height)
tower2 = Tower(screen, red, 600, 600, 25, 25, width, height)
towers = [tower1, tower2]
path = Path(screen, height, width, 50, 50)
wave = CreepWave(screen, 'fast', currentWave, path.creepPath)
clock = pygame.time.Clock()

while running:
    time = timeit.default_timer()
    clock.tick(60)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 3:
            print "right mouse" 
        else:
            print "mouse, but not right!"

    screen.fill((black))
    path.draw()
    wave.updateCreeps()
    if wave.waveOver():
        currentWave += 1
        wave = CreepWave(screen, 'fast', currentWave)

    for tower in towers:
        tower.update(wave.creeps, time)
        for bullet in tower.bullets:
            try:
                for creep in wave.creeps:
                    if bullet.rect.colliderect(creep.rect):
                        creep.attacked(25)
                        if creep.health < 1:
                            wave.creeps.remove(creep)
                            tower.bullets.remove(bullet)
            except:
                print "eh"

    pygame.display.flip()

    time += 1