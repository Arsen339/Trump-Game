from Sound import *
import Parametrs as pr
from FileWorkClass import *


#Class for cheat button
class Button:
    
    def __init__(self, width, height):
        
        self.width = width
        self.height = height
        self.inactive_color = (200,190,140)
        self.active_color = (180,255,100)
    #Draws button    
    def draw(self, x, y, message):
        #global LiveCounter
       
        #Gets mouse's position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(pr.win, self.active_color, (x, y, self.width, self.height))
                pygame.display.update()
                if click[0] == 1:
                    pygame.mixer.Sound.play(BS)
                    pygame.time.delay(300)
                    Stats.LiveCounter +=1
        else:
            pygame.draw.rect(pr.win, self.inactive_color, (x, y, self.width, self.height ))
            pygame.display.update()
    #Prints message        
    def print_but_mes(self, x, y, font_color = (125, 0, 155), font_type = 'BantyBold.ttf', font_size = 30):
        font_type=pygame.font.Font(font_type, font_size)
        text=font_type.render("cheat", True, font_color)
        pr.win.blit(text, (x,y)) 
        pygame.display.update()