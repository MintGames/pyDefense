import pygame
import math
import random

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0

class Path:
    def __init__(self, screen, height, width, tileSizeX, tileSizeY):
        print "whatever"
        self.screen = screen
        self.screenHeight = height
        self.screenWidth = width
        self.squaresX = self.screenHeight / tileSizeX
        self.squaresY = self.screenWidth / tileSizeY
        self.tileSizeX = tileSizeX
        self.tileSizeY = tileSizeY
        self.path = []
        self.startSqaure = (0, random.randint(1, self.squaresY - 1))
        self.path.append(self.startSqaure)
        finish = False
        lastPathPos = self.startSqaure
        lastPathDir = "null"
        while finish == False:
            randomNumber = random.randint(1, 3)
            if randomNumber == 1 and lastPathDir != "down" and (lastPathPos[1] - 1) < 0:
                self.path.append((lastPathPos[0], lastPathPos[1] - 1))
                lastPathPos = (lastPathPos[0], lastPathPos[1] - 1)
                lastPathDir = "up"
            elif randomNumber == 2 and lastPathDir != "up" and (lastPathPos[1] + 1) < self.squaresY:
                self.path.append((lastPathPos[0], lastPathPos[1] + 1))
                lastPathPos = (lastPathPos[0], lastPathPos[1] + 1)
                lastPathDir = "down"
            elif randomNumber == 3:
                self.path.append((lastPathPos[0] + 1, lastPathPos[1]))
                lastPathPos = (lastPathPos[0] + 1, lastPathPos[1])
                lastPathDir = "right"
            lastPathPos = (lastPathPos[0], lastPathPos[1])
            if lastPathPos[0] == self.squaresX:
                finish = True
        self.creepPath = []
        for tile in self.path:
            self.creepPath.append((tile[0] * self.tileSizeX + self.tileSizeX / 2, tile[1] * self.tileSizeY + self.tileSizeY / 2))

    def draw(self):
        for tile in self.path:
            pygame.draw.rect(self.screen, red, (tile[0] * self.tileSizeX, tile[1] * self.tileSizeY,
            self.tileSizeX, self.tileSizeY))