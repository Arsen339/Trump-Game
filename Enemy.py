from Parametrs import win
import pygame
# class for enemies
class enemy():
    def __init__(self, x, y, radius, speed, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.facing = facing
    #drawing enemy in window
    def DrawEnemy(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)