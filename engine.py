#airHockey pygame

import pygame
import math
pygame.init()

size = width, height = 700, 900
screen = pygame.display.set_mode((size))
running = 1

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0

time = 0

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
            if (bullet.direction == 1 and bullet.currentPosX > bullet.endPosX) or (bullet.direction == -1 and bullet.currentPosX < bullet.endPosX):
                self.bullets.remove(bullet)
            bullet.update()

    def shoot(self, mousePos):
        bullet = Bullet(self.centre, mousePos)
        self.bullets.append(bullet)


class Bullet:

    def __init__(self, (startPosX, startPosY), (endPosX, endPosY)):
        global time
        self.startTime = 0
        self.startPosX = startPosX
        self.startPosY = startPosY
        self.endPosX = endPosX
        self.endPosY = endPosY
        self.currentPosX = self.startPosX
        self.currentPosY = self.startPosY
        self.rect = pygame.Rect(self.startPosX, self.startPosY, self.endPosX, self.endPosY)
        print str((self.startPosY - self.endPosY)) + " Divided by " + str((self.startPosX - self.endPosX))
        self.gradient = (self.startPosY - self.endPosY) / float((self.startPosX - self.endPosX))
        print self.gradient
        self.speed = 3
        if self.endPosX < self.startPosX:
            self.direction = -1
        else:
            self.direction = 1

    def update(self):
        self.currentPosX += math.cos(math.atan(self.gradient))*self.speed*self.direction
        self.currentPosY += math.sin(math.atan(self.gradient))*self.speed*self.direction
        pygame.draw.line(screen, white, (self.currentPosX, self.currentPosY), (self.startPosX, self.startPosY))



tower1 = Tower(screen, red, 100, 100, 25, 25)
tower2 = Tower(screen, red, 600, 600, 25, 25)
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    if event.type == pygame.MOUSEBUTTONUP:
        tower1.shoot(pygame.mouse.get_pos())
        tower2.shoot(pygame.mouse.get_pos())

    screen.fill((black))

    tower1.update()
    tower2.update()

    pygame.display.flip()
    time += 1
