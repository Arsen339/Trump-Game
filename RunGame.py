#Adding modules
import pygame
import random
import math
from Enemy import *
from GamePlayFuns import *
from Gamer import *
from Parametrs import *
from Images import *
from Snaryad import *
from Sound import *

#Initializing pygame
pygame.init()


#Main
run  = True

#creating FunRunner class
NewGame = FunRunner(1)


while run:
    clock.tick(30)
    #Repeating in MS
    pygame.time.delay(50)
    #Out when close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    NewGame.pause()
    NewGame.BulletMove()
    NewGame.PlayerJumping()
    NewGame.PlayerMoving()
    NewGame.EnemySetting()
    NewGame.drawWindow()
    NewGame.Losing()
    

pygame.quit()









