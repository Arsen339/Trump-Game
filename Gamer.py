import pygame



#Class for gamer
class Gamer():
    def __init__(self,XPos,YPos, LeftFacing, RightFacing, lastMove, GamerSpeed, InAirNow, HeightCount):
        
        self.XPos = XPos
        self.YPos = YPos
        self.LeftFacing = LeftFacing
        self.Rightfacing = RightFacing
        self.lastMove = lastMove
        self.GamerSpeed = GamerSpeed
        self.InAirNow = InAirNow
        self.HeightCount = HeightCount

        
Trump=Gamer(50, 429, False, False, "right", 7, False, 10)