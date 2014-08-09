import pygame
import math
import random

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0


class CreepWave:
    def __init__(self, screen, typeOfWave, waveLevel):
        self.screen = screen
        self.typeOfWave = typeOfWave
        self.waveLevel = waveLevel
        self.creeps = []
        if typeOfWave == 'fast':
            self.fastWave()
        elif typeOfWave == 'tank':
            self.tankWave()
        elif typeOfWave == 'swarm':
            self.swarmWave()
        elif typeOfWave == 'healing':
            self.healingWave()
        elif typeOfWave == 'boss':
            self.bossWave()
            

    def fastWave(self):
        for i in range(5):
            creep = Creep(self.screen, blue, (0, random.randint(0,400)), (20, 20), 6, 50)
            self.creeps.append(creep)

    def tankWave(self):
        print "yeah"

    def swarmWave(self):
        print "yeah"

    def healingWave(self):
        print "yeah"

    def bossWave(self):
        print "yeah"

    def updateCreeps(self):
        for creep in self.creeps:
            creep.updatePosition()
            creep.drawCreep(self.screen)

    def waveOver(self):
        if len(self.creeps) <= 1:
            return True
        else:
            return False

class Creep:
    def __init__(self, screen, colour, (startPosX, startPosY), (sizeX, sizeY), speed, health):
        self.startPosX = startPosX
        self.startPosY = startPosY
        self.currentPosX = self.startPosX
        self.currentPosY = self.startPosY
        self.health = health
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.stageOfPath = 0
        self.path = [(500,600), (400,100), (200,100), (60, 800), (700, 90), (500,600), (400,100), (200,100), (60, 800), (700, 90), (500,600), (400,100), (200,100), (60, 800), (700, 90)]
        self.speed = speed
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