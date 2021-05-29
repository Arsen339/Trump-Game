import pygame

class Gamer:
    """Class for gamer """
    def __init__(self, XPos, YPos, left_facing, right_facing, last_move, gamer_speed, in_air_now, height_count):
        
        self.XPos = XPos
        self.YPos = YPos
        self.left_facing = left_facing
        self.right_facing = right_facing
        self.last_move = last_move
        self.gamer_speed = gamer_speed
        self.in_air_now = in_air_now
        self.height_count = height_count

        
Trump = Gamer(50, 429, False, False, "right", 7, False, 10)