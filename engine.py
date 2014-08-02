''' TODO:
Make so missiles despawn off map instead of destination
Make creeps travel with A*
Gives creeps health bars
Make missile take off health when contact
'''

import pygame
import math
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

    def attacked(self, damage):
        self.health -= damage

    def update(self):
        self.currentPosX += 0.1
        self.healthRectRed = pygame.Rect(self.currentPosX - 10 + self.health / 5, self.currentPosY - 15, (100 - self.health) / 5, 3)
        self.healthRectGreen = pygame.Rect(self.currentPosX - 10, self.currentPosY - 15, self.health / 5, 3)
        self.rect = pygame.Rect(self.currentPosX - 10, self.currentPosY - 10, 20, 20)
        pygame.draw.rect(screen, blue, self.rect)
        pygame.draw.rect(screen, red, self.healthRectRed)
        pygame.draw.rect(screen, green, self.healthRectGreen)



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
        global height
        global width
        pygame.draw.rect(screen, red, self.rect)
        print "There are bullets: " + str(len(self.bullets))
        for bullet in self.bullets:
            if (bullet.currentPosX > width) or (bullet.currentPosY > height) or (bullet.currentPosX < 0) or (bullet.currentPosY < 0):
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
        self.rect = pygame.Rect(self.currentPosX - 5, self.currentPosY - 5, 10, 10)
        pygame.draw.circle(screen, white, (int(self.currentPosX), int(self.currentPosY)), 5)



tower1 = Tower(screen, red, 100, 100, 25, 25)
tower2 = Tower(screen, red, 600, 600, 25, 25)
towers = [tower1, tower2]
creep1 = Creep(screen, blue, (0, 350), (0, 350))
creep2 = Creep(screen, blue, (0, 400), (0, 400))
creep3 = Creep(screen, blue, (0, 450), (0, 450))
creeps = [creep1, creep2, creep3]
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
    for creep in creeps:
        creep.update()

    for tower in towers:
        tower.update()
        for bullet in tower.bullets:
            for creep in creeps:
                if bullet.rect.colliderect(creep.rect):
                    creep.attacked(25)
                    if creep.health < 1:
                        creeps.remove(creep)
                    tower.bullets.remove(bullet)

    pygame.display.flip()
    time += 1
