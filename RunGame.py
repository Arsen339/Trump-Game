# Adding modules
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
from ButtonClass import *
from FileWorkClass import *

# Initializing pygame
pygame.init()


# Main
run = True

# Creating FunRunner class
NewGame = FunRunner(1)


while run:
    clock.tick(30)
    # Repeating in MS
    pygame.time.delay(50)
    # Out when close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    NewGame.pause()
    NewGame.bullet_move()
    NewGame.player_jumping()
    NewGame.player_moving()
    NewGame.enemy_setting()
    NewGame.draw_window()
    NewGame.losing()
    NewBut = Button(80, 80)
    NewBut.draw(400, 20, " ") 
    NewBut.print_but_mes(400, 20)
    NewGame.save_data(Stats.LiveCounter, Stats.PointCounter)
    NewGame.restart_game()
pygame.quit()









