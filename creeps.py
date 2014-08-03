import pygame
import math

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0

class Creep:
    def __init__(self, screen, colour, (startPosX, startPosY), (endPosX, endPosY)):
        self.startPosX = startPosX
        self.startPosY = startPosY
        self.endPosX = endPosX
        self.endPosY = endPosY
        self.currentPosX = self.startPosX
        self.currentPosY = self.startPosY
        self.rect = pygame.Rect(self.startPosX, self.startPosY, self.endPosX, self.endPosY)
        self.health = 100
        self.stageOfPath = 0
        self.path = [(500,600), (400,100), (200,100), (60, 800), (700, 90), (500,600), (400,100), (200,100), (60, 800), (700, 90), (500,600), (400,100), (200,100), (60, 800), (700, 90)]
        self.speed = 3
        self.targetDestination()

    def attacked(self, damage):
        self.health -= damage

    def targetDestination(self):
        self.endPosX, self.endPosY = self.path[self.stageOfPath]
        if self.endPosX < self.currentPosX:
            self.direction = -1
        else:
            self.direction = 1
        self.gradient = (self.currentPosY - self.endPosY) / float((self.currentPosX - self.endPosX))
        self.targetDestinationRect = pygame.Rect(self.endPosX - 2, self.endPosY - 2, 4, 4)

    def updatePosition(self):
        self.rect = pygame.Rect(self.currentPosX - 10, self.currentPosY - 10, 20, 20)
        if self.rect.colliderect(self.targetDestinationRect):
            self.stageOfPath += 1
            self.targetDestination()
        self.currentPosX += math.cos(math.atan(self.gradient))*self.speed*self.direction
        self.currentPosY += math.sin(math.atan(self.gradient))*self.speed*self.direction


        self.healthRectRed = pygame.Rect(self.currentPosX - 10 + self.health / 5, self.currentPosY - 15, (100 - self.health) / 5, 3)
        self.healthRectGreen = pygame.Rect(self.currentPosX - 10, self.currentPosY - 15, self.health / 5, 3)



    def updatePath(self, newPath):
        self.path = newPath

    def drawCreep(self, screen):
        pygame.draw.rect(screen, blue, self.rect)
        pygame.draw.rect(screen, red, self.healthRectRed)
        pygame.draw.rect(screen, green, self.healthRectGreen)