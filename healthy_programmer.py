#Healthy programer:-

#assume that a programmer works at office from 9am to 5pm.we have to take care of his health
#and remind him three things.

# 1. to drink water every 40 minutes.
# 2. to do eye excersise after every 30 minutes.
# 3. to perform physical activity after every 45 minutes.

# instructions:-

# the task is to create a program that plays mp3 audio untill the programmer enters the
# input which implies that he has done the task.

# for water user should enter 'drank'
# for eye excersise user should enter 'eyDone'
# for physical activity user should enter 'exDone'

# after the user enter the input, a log file should be created listing all the tasks done.

# challenges;-

# you will have to manage the clashes between the remainders such that no two remainders
# plays at the same time.
# use pygame module to play audio.

from pygame import mixer
from datetime import  datetime
from time import time

def music_on_loop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
      user_input = input("Type here")
      user_input = user_input.lower()
      if user_input == stopper:
        mixer.music.stop()
        break

def log(msg):
    with open("timings.txt","a") as f:
        f.write(f"\n{msg} {datetime.now()}")

if __name__ == '__main__':
    initial_water = time()#water,eyes,physical ke initial time ko current time ke brabr
    initial_eyes = time()#krdiye hai
    initial_exercise = time()

    water_secs = 40*60 #40*60 means har 40 minute me paani pina padega.
    eye_secs = 30*60 #30*60 means har 30 minute me eyes ka exercise karna padega.
    phy_exc_secs = 45*60 #45*60 means har 45 minute me physical exercise karna padega.

    while True:
        if time() - initial_water > water_secs:#initial time ko current time se minus krke 40 minute se greater kare hai.
            print("Water drinking time. Enter 'drank' to stop the alarm\n")
            music_on_loop("drinks_on_me.mp3","drank")
            initial_water = time() #firse initial time set hojyga water ka
            log("Drank water at:")

        if time() - initial_eyes > eye_secs:
            print("Eyes excersise time. Enter 'eydone' to stop the alarm\n")
            music_on_loop("devils_eyes.mp3","eydone")
            initial_eyes = time() #firse initial time set hojyga eye exercise ka
            log("Done eyes excersise at:")

        if time() - initial_exercise > phy_ex_secs:
            print("Physical excersise time.Enter 'exdone' to stop the alarm\n")
            music_on_loop("turn_down_for_what.mp3","exdone")
            initial_exercise= time() #firse initial time set hojyga physical exercise ka
            log("Done physical excersise at:")
