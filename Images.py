
import pygame
pygame.init()
#Uploading pictures of sprites in array
walkRight=[pygame.image.load("pictures/pygame_right_1.png"), pygame.image.load("pictures/pygame_right_2.png"),
pygame.image.load("pictures/pygame_right_3.png"), pygame.image.load("pictures/pygame_right_4.png"),
pygame.image.load("pictures/pygame_right_5.png"), pygame.image.load("pictures/pygame_right_6.png")]

walkLeft=[pygame.image.load("pictures/pygame_left_1.png"), pygame.image.load("pictures/pygame_left_2.png"),
pygame.image.load("pictures/pygame_left_3.png"), pygame.image.load("pictures/pygame_left_4.png"),
pygame.image.load("pictures/pygame_left_5.png"), pygame.image.load("pictures/pygame_left_6.png")]


#Loading default player's stand
playerStand = pygame.image.load("pictures/pygame_idle.png")

#Loading screenWallPaper
bg = pygame.image.load("pictures/bg.jpg")