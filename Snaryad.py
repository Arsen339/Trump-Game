from Parametrs import win
import pygame

#class for bullets
class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing
    #drawing bullets in window
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
