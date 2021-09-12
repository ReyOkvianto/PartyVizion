#0 people - no music
#1 person - classical/lofi
#2-3 people - leon bridges, alternative, common pop
#4 or more - party music
from pygame import mixer  # Load the popular external library
import time
import random

#Initialize the mixer
music_player = mixer.init()

level1 = ["./mp3/le-festin.mp3", "./mp3/viatecture.mp3", "./mp3/saveALife.mp3"]
level2 = ["./mp3/WayYouAre.mp3", "./mp3/BELONGwME.mp3", "./mp3/rich-girl.mp3", "./mp3/partyUSA.mp3"]
level3 = ["./mp3/Down.mp3", "./mp3/MOBAMBA.mp3", "./mp3/CRANKdat.mp3"]

def peopleInRoom():
    return random.choice([level1, level2, level3])

def testMusic():

    mixer.music.load(random.choice(peopleInRoom()))
    # mixer.music.load(random.choice(level3))
    mixer.music.play()
    time.sleep(10)
    mixer.music.pause()

testMusic()

# import vlc
# p = vlc.MediaPlayer("Down.mp3")
# p.play()


# def playMusic():
#         print("10 people are in the room, begin playing")
#         p = vlc.MediaPlayer("Down.mp3")
#         p.play()



# command = None
# while command != "quit":
#     command = input("Enter 0, 1, or quit: ")
#     if (command == "0"):
#         playMusic()
#     elif (command == "1"):
#         print("No music requested to be played")
#     elif (command == "quit"):

# command = None
# p = vlc.MediaPlayer("Down.mp3")
# command = input("Enter something: ")
# while command != "quit":
#     if (command == "play"):
#         p.play()
#     elif (command == "stop"):
#         p.stop()
#     command = input("Enter something: ")

