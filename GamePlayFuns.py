import pygame
pygame.init()
from Gamer import *
import Parametrs as pr
import random
from Images import *
from Enemy import *
from Snaryad import *
from Sound import * 
from FileWorkClass import *


class FunRunner:
    """Class consists of gameplay funs"""
    def __init__(self, flag):
        self.flag = flag    

    def draw_window(self):
        """Update window fun """
        
        # WindowSet
        win.blit(bg, (0, 0))
        # pygame.draw.rect(win, (0,0,255), (x, y, width, height))- draws rectangle instead of player
        # win.fill((0,0,0))-Paint the screen black
        # Global var used in any part of code
        
        # Every sprite played in 5 shots. 30 shots aset as maximal
        if pr.animCount + 1 > 30:
            pr.animCount = 0
        if Trump.left_facing:
            win.blit(walkLeft[pr.animCount // 5], (Trump.XPos, Trump.YPos))
            pr.animCount += 1
        elif Trump.right_facing:
            win.blit(walkRight[pr.animCount // 5], (Trump.XPos, Trump.YPos))
            pr.animCount += 1
        else:
            win.blit(playerStand, (Trump.XPos, Trump.YPos))
        for bullet in pr.bullets:
            bullet.draw(win)
        for danger in pr.dangers:
            danger.draw_enemy(win)
        self.print_text("TRUMP GAME!", 100, 100)

        ScoreSkill = ("Points: " + str(Stats.PointCounter))

        self.print_text(ScoreSkill, 100, 50)

        LiveSkill = ("Lives: " + str(Stats.LiveCounter))    
        self.print_text(LiveSkill, 100, 20)

        pygame.display.update()

    def enemy_setting(self):
        """Function creates and deletes anemies  """
        ChoiceAbility = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        EnemyRadius = random.choice([35, 39])
        EnemySpeed = random.choice([1, 2, 3])
        # adds an enemy
        if random.choice(ChoiceAbility) == 9 and len(pr.dangers) < pr.MaxEnemies:
            pr.dangers.append(Enemy(0, 500 - EnemyRadius, EnemyRadius, EnemySpeed, (255, 100, 180), 1))
        elif random.choice(ChoiceAbility) == 10 and len(pr.dangers) < pr.MaxEnemies:
            pr.dangers.append(Enemy(500, 500 - EnemyRadius, EnemyRadius, - EnemySpeed, (0, 255, 0), -1))
        # moving and deleting enemies
        if len(pr.dangers) >=1:  
            for danger in pr.dangers: 
                if danger.x < 500 and danger.facing == 1:
                    danger.x += danger.speed
                elif danger.x > 0 and danger.facing == -1:
                    danger.x += danger.speed
                else:
                    pr.dangers.pop(pr.dangers.index(danger))
        # killing enemies            
        if len(pr.bullets) >=1:           
            for bullet in pr.bullets.copy():
                for danger in pr.dangers.copy():
                    if abs(bullet.x-danger.x) <5 and abs(bullet.y-danger.y) < 45:
                            Stats.PointCounter +=1
                        # We check copies to avoid memory mistakes
                            pr.dangers.pop(pr.dangers.index(danger))
                            pygame.mixer.Sound.play(SS)
                            bullet.x = 0
                            bullet.y = 0
                            pr.bullets.remove(bullet)
                        

    def player_moving(self):
        """Fun for player Moving """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and Trump.XPos > 5:
            Trump.XPos -= Trump.gamer_speed
            Trump.left_facing = True
            Trump.right_facing = False
            Trump.last_move = "left"
        elif keys[pygame.K_RIGHT] and Trump.XPos < 500-5-pr.width:
            Trump.XPos += Trump.gamer_speed
            Trump.left_facing = False
            Trump.right_facing = True
            Trump.last_move = "right"
        else:
            Trump.left_facing = False
            Trump.right_facing = False
            pr.animCount = 0


    def player_jumping(self):
        """Fun for jump """
        keys = pygame.key.get_pressed()
        if not Trump.in_air_now:
        
            if keys[pygame.K_SPACE]:
                Trump.in_air_now = True
        else:
            
            if Trump.height_count >= -10:
                if Trump.height_count < 0:
                    Trump.YPos += (Trump.height_count ** 2) / 2
                else:
                    Trump.YPos -= (Trump.height_count ** 2) / 2
                Trump.height_count -= 1
            else:
                Trump.in_air_now = False
                Trump.height_count = 10

    def bullet_move(self):
        """Fun for bullet  """
        for bullet in pr.bullets.copy():
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                pr.bullets.pop(pr.bullets.index(bullet))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            if Trump.last_move == "right":
                facing = 1
            else:
                facing = -1
            if len(pr.bullets) < pr.MaxBullet:
                pr.bullets.append(Snaryad(round(Trump.XPos + pr.width // 2), round(Trump.YPos + pr.height // 2), 5, (255, 0, 0), facing))



    def losing(self):
        """Fun for Losing """
        for danger in pr.dangers:
            if abs(Trump.XPos-danger.x) < danger.radius+5  and abs(Trump.YPos-danger.y) < danger.radius * 2:
                Stats.LiveCounter -= 1
                if Stats.LiveCounter <=0:
                    pr.run = False
                    quit()

    def print_text(self, message, x, y, font_color=(0, 0, 0), font_type='BantyBold.ttf', font_size=30):
        """Function for printing text on the screen   """
        font_type=pygame.font.Font(font_type, font_size)
        text=font_type.render(message, True, font_color)
        win.blit(text, (x,y))
        


    def save_data(self, LiveCounterLocal, PointCounterLocal):
        """Сохраняет прогресс"""
        if Stats.SaveFlag == 1:
            NewData = ['']*3
            NewData[2] = str(PointCounterLocal)
            NewData[1] = "\n"
            NewData[0] = str(LiveCounterLocal)
            f=open('saves.txt', 'w')
            f.writelines(NewData)
            f.close()

        if Stats.SaveFlag == 2:
            NewData = ['']*3
            NewData[0] = "100"
            NewData[1] = "\n"
            NewData[2] = "0"
               

            f = open('saves.txt', 'w')
            f.writelines(NewData)
            f.close()
        Stats.SaveFlag = 0








    def pause(self):
        """Function for pause """
        
        keys = pygame.key.get_pressed()
        paused = True
        if keys[pygame.K_w]:

            Stats.SaveFlag = 1
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pr.run = False
                        quit()

                self.print_text('pause. Press S to continue', 150, 150)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_s]:
                    paused = False
                    
                pygame.display.update()
                #clock.tick(15)
              
    

    def restart_game(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            Stats.SaveFlag=2
            Trump.XPos=50
            Trump.Ypos=429
            Stats.PointCounter=0
            Stats.LiveCounter=100
            for danger in pr.dangers.copy():
                pr.dangers.pop(pr.dangers.index(danger))
                