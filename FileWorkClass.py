#Class for working with the stats file
class FileWork():
    def __init__(self, LiveCounter, PointCounter, SaveFlag):
        self.LiveCounter =LiveCounter
        self.PointCounter = PointCounter
        self.SaveFlag = SaveFlag
        
#Opening and copying the data from file        
f = open('saves.txt', 'r+')
LiveFromFile = f.readline()
PointFromFile = f.readline()

print(LiveFromFile)
print(PointFromFile)
OldData=f.read()
f.close()

PointFromFile = int(PointFromFile)
LiveFromFile = int(LiveFromFile)
#Creating Stats Class
Stats=FileWork(LiveFromFile, PointFromFile, 0)