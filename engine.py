#airHockey pygame

import pygame
pygame.init()

size = width, height = 700, 900
screen = pygame.display.set_mode((size))
running = 1

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0

class Tower:

    def __init__(self, screen, colour, positionX, positionY, sizeX, sizeY):
        self.colour = colour
        self.positionX = positionX
        self.positionY = positionY
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.centreX = positionX + sizeX / 2
        self.centreY = positionY + sizeY / 2
        self.centre = self.centreX, self.centreY
        self.rect = pygame.Rect(self.positionX, self.positionY, self.sizeX, self.sizeY)
        self.bullets = []

    def update(self):
        pygame.draw.rect(screen, red, self.rect)
        for bullet in self.bullets:
            bullet.update()

    def shoot(self, mousePos):
        bullet = Bullet(self.centre, mousePos)
        self.bullets.append(bullet)


class Bullet:

    def __init__(self, startPos, endPos):
        self.startPosX, self.startPosY = startPos
        self.endPosX, self.endPosY = endPos
        self.rect = pygame.Rect(self.startPosX, self.startPosY, self.endPosX, self.endPosY)

    def update(self):
        pygame.draw.line(screen, white, (self.startPosX, self.startPosY), (self.endPosX, self.endPosY))



tower1 = Tower(screen, red, 100, 100, 25, 25)

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    if event.type == pygame.MOUSEBUTTONUP:
        tower1.shoot(pygame.mouse.get_pos())

    screen.fill((black))

    tower1.update()

    pygame.display.flip()
