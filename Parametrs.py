
import pygame
pygame.init()
# Setting the display
win =pygame.display.set_mode((500, 500))
pygame.display.set_caption("Cubes game")

# Constants
clock = pygame.time.Clock()

# player's size and speed
width = 60
height = 71

# Lives and kills counter
# PointCounter = 0
# LiveCounter = 100

animCount = 0


run = True
# Maximum allowed bullets and enemies
MaxBullet = 1
MaxEnemies = 4


# Arrays for bullets and enemies
bullets = []
dangers = []



