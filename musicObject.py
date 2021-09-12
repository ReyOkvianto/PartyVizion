from pygame import mixer  # Load the popular external library
from time import sleep
import random
from threading import *
class music(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.numPeople = 0

    def getNumPeople(self):
        return self.numPeople
    
    def setNumPeople(self,numPeople):
        self.numPeople = numPeople
    
    def testMusic(self,NumPeopleFunction):
        mixer.init()
        level1 = ["./mp3/le-festin.mp3", "./mp3/viatecture.mp3", "./mp3/saveALife.mp3"]
        level2 = ["./mp3/WayYouAre.mp3", "./mp3/BELONGwME.mp3", "./mp3/rich-girl.mp3", "./mp3/partyUSA.mp3"]
        level3 = ["./mp3/Down.mp3", "./mp3/MOBAMBA.mp3", "./mp3/CRANKdat.mp3"]
        
        
        
        while True:
            numPeople = NumPeopleFunction()
            print("in the MUSIC CODE" , numPeople)
            if numPeople != self.getNumPeople():
                self.numPeople = numPeople
                if numPeople == 1:
                    mixer.music.load(random.choice(level1))
                    mixer.music.play(0)
                    sleep(15)
                     
                if numPeople == 2:
                    mixer.music.load(random.choice(level2))
                    mixer.music.play(0)
                    sleep(15)
                    
                if numPeople >= 3:
                    mixer.music.load(random.choice(level3))
                    mixer.music.play(0)
                    sleep(15)
                    
                else:
                    mixer.music.stop()
                    print("should pause")
            else:
                if numPeople != 0:
                    continue
                else:
                    mixer.music.stop()
            
        