import random
import time

import pyttsx4

if __name__ == '__main__':
    engine1 = pyttsx4.init()  # object creation
    map_ = {}
    map_[0] = "o"
    map_[1] = "one"
    map_[2] = "two"
    map_[3] = "three"
    map_[4] = "four"
    map_[5] = "five"
    map_[6] = "six"
    map_[7] = "seven"
    map_[8] = "eight"
    map_[9] = "nine"
    map_[10] = "double"
    map_[11] = "triple"
    # rate = engine1.getProperty('rate')  # getting details of current speaking rate
    # print(rate)
    # engine1.setProperty('rate', 450)
    for _ in range(1, 100):
        x = random.randint(0, 11)
        y = random.randint(0, 11)
        z = random.randint(0, 11)
        m = random.randint(0, 11)
        x1 = random.randint(0, 11)
        y1 = random.randint(0, 11)
        z1 = random.randint(0, 11)
        m1 = random.randint(0, 11)
        engine1.say(map_[x])
        engine1.say(map_[y])
        engine1.say(map_[z])
        engine1.say(map_[m])
        engine1.say(map_[x1])
        engine1.say(map_[y1])
        engine1.say(map_[z1])
        engine1.say(map_[m1])
        print(x, y, z, m, x1, y1, z1, m1)
        # engine1.say(map_[random.randint(0, 9)])
        # engine1.say(map_[random.randint(0, 9)])
        # engine1.say(map_[random.randint(0, 9)])
        # engine1.say(map_[random.randint(0, 9)])
        # engine1.say(map_[random.randint(4, 9)])
        time.sleep(
            0.5
        )

        engine1.runAndWait()

# """ RATE"""
# rate = engine.getProperty('rate')  # getting details of current speaking rate
# print(rate)  # printing current voice rate
# engine.setProperty('rate', 125)  # setting up new voice rate

# """VOLUME"""
# volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
# print(volume)  # printing current volume level
# engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
#
# """VOICE"""
# voices = engine.getProperty('voices')  # getting details of current voice
# # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
#
# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()
#
# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()
