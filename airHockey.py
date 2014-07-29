#airHockey pygame

import pygame
import math
pygame.init()

size = width, height = 700, 900
screen = pygame.display.set_mode((size))
running = 1

black = 0, 0, 0
red = 255, 0, 0

pos_a = (100, 100)
pos_b = (600, 100)
pos_c = (600, 800)
pos_d = (100, 800)

def degreesToRadians(deg):
    return deg/180.0 * math.pi

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0

	screen.fill((black))

	pygame.draw.line(screen, red, (200, 100), (500, 100), 5)
	pygame.draw.line(screen, red, (600, 200), (600, 700), 5)
	pygame.draw.line(screen, red, (500, 800), (200, 800), 5)
	pygame.draw.line(screen, red, (100, 700), (100, 200), 5)

	pygame.draw.arc(screen, red, ((100, 100), (200, 200)), (math.pi / 2), (math.pi), 5)
	pygame.draw.arc(screen, red, ((500, 100), (500, 200)), (3 * math.pi / 2), (math.pi), 5)

	pygame.display.flip()
