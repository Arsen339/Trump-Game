from Parametrs import win
import pygame

class Enemy:
    """class for enemies-circles """
    def __init__(self, x, y, radius, speed, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.facing = facing

    def draw_enemy(self, win):
        """Drawing enemy on window """
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)