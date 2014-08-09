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


while True:
	events = pygame.event.get()
	for event in events:
	    if event.type == pygame.KEYDOWN:
	        print pygame.key.get_pressed()