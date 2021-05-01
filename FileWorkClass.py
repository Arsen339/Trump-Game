#Class for gamer
class FileWork():
    def __init__(self, LiveCounter, PointCounter, SaveFlag):
        self.LiveCounter =LiveCounter
        self.PointCounter = PointCounter
        self.SaveFlag = SaveFlag
        
f = open('saves.txt', 'r+')
LiveFromFile = f.readline()
PointFromFile = f.readline()

print(LiveFromFile)
print(PointFromFile)
OldData=f.read()
f.close()

PointFromFile = int(PointFromFile)
LiveFromFile = int(LiveFromFile)

Stats=FileWork(LiveFromFile, PointFromFile, 0)