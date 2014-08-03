import pygame
import math
import random

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0

class Tower:

    def __init__(self, screen, colour, positionX, positionY, sizeX, sizeY, screenWidth, screenHeight):
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
        self.screen = screen
        self.width = screenWidth
        self.height = screenHeight

    def update(self):
        global height
        global width
        pygame.draw.rect(self.screen, red, self.rect)
        print "There are bullets: " + str(len(self.bullets))
        for bullet in self.bullets:
            if (bullet.currentPosX > self.width) or (bullet.currentPosY > self.height) or (bullet.currentPosX < 0) or (bullet.currentPosY < 0):
                self.bullets.remove(bullet)
            bullet.update()

    def shoot(self, mousePos):
        bullet = Bullet(self.centre, mousePos, self.screen)
        self.bullets.append(bullet)


class Bullet:

    def __init__(self, (startPosX, startPosY), (endPosX, endPosY), screen):
        global time
        self.startTime = 0
        self.startPosX = startPosX
        self.startPosY = startPosY
        self.endPosX = endPosX
        self.endPosY = endPosY
        self.currentPosX = self.startPosX
        self.currentPosY = self.startPosY
        self.rect = pygame.Rect(self.startPosX, self.startPosY, self.endPosX, self.endPosY)
        self.screen = screen
        self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
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
        self.rect = pygame.Rect(self.currentPosX - 5, self.currentPosY - 5, 10, 10)
        pygame.draw.circle(self.screen, self.colour, (int(self.currentPosX), int(self.currentPosY)), 5)