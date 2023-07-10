#########################################################################################
# Get Started:
# pip install -r requirements.txt

import os
import time
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"  # Hide Pygame initialization message
import pygame
from tqdm import tqdm

#########################################################################################

print(""" 
 ___  __  __  _    _ 
(__ )(  \/  )( \/\/ )
 / /  )    (  \    / 
(_/  (_/\/\_)  \/\/  
""")

#########################################################################################

# # The 7-minute workout is a form of high-intensity interval training (HIIT) that offers a quick and efficient way to get a full-body workout. It was developed by Brett Klika and Chris Jordan, and it gained popularity due to its simplicity and time-saving nature.

# The workout consists of 12 exercises, each performed for 30 seconds with a 10-second rest period in between. These exercises target different muscle groups and provide a cardiovascular challenge. 

# The idea behind the 7-minute workout is to perform each exercise with maximum effort within the given time frame. It offers a quick and intense workout that can be done almost anywhere, making it a convenient option for individuals with busy schedules or limited time for exercise.

# In the traditional 7-minute workout, there is a 10-second rest period between each exercise. This short rest period allows for a quick recovery and transition to the next exercise. It is important to note that the workout is designed to be fast-paced and intense, so it's recommended to use the rest periods efficiently by preparing for the next exercise and catching your breath before moving on.

# Exercise 1: Jumping Jacks (25 seconds) + Rest (10 seconds) = 35 seconds
# Exercise 2: Wall Sit (25 seconds) + Rest (10 seconds) = 35 seconds
# Exercise 3: Push-Ups (25 seconds) + Rest (10 seconds) = 35 seconds
# Exercise 4: Abdominal Crunches (25 seconds) + Rest (10 seconds) = 35 seconds
# Exercise 5: Step-Ups onto a Chair (25 seconds) + Rest (10 seconds) = 35 seconds
# Exercise 6: Squats (25 seconds) + Rest (10 seconds) = 35 seconds
# Exercise 7: Tricep Dips on a Chair (25 seconds) + Rest (10 seconds) = 35 seconds
# Exercise 8: Plank (25 seconds) + Rest (10 seconds) = 35 seconds
# Exercise 9: High Knees (25 seconds) + Rest (10 seconds) = 35 seconds
# Exercise 10: Lunges (25 seconds) + Rest (10 seconds) = 35 seconds
# Exercise 11: Push-Up with Rotation (25 seconds) + Rest (10 seconds) = 35 seconds
# Exercise 12: Side Plank (25 seconds) + Rest (10 seconds) = 35 seconds

#########################################################################################

def exercise(seconds, message):
    print("", flush=True)
    print(f"{seconds} {message}", flush=True)
    time.sleep(1)
    with tqdm(total=seconds, desc="Rest", unit="s") as pbar:
        for i in reversed(range(seconds)):
            time.sleep(1)
            pbar.update()
            pbar.set_description(f"{i} seconds")
    print("Rest!", flush=True)
    audio_file = os.path.join(os.path.dirname(__file__), "sfx/Ring06.wav")
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    time.sleep(1)
    
def rest(seconds, message):
    print("", flush=True)
    print(f"{seconds} {message}", flush=True)
    time.sleep(1)
    with tqdm(total=seconds, desc="Rest", unit="s") as pbar:
        for i in reversed(range(seconds)):
            time.sleep(1)
            pbar.update()
            pbar.set_description(f"Rest: {i} seconds")
    print("Time's up!", flush=True)
    audio_file = os.path.join(os.path.dirname(__file__), "sfx/Windows Unlock.wav")
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    time.sleep(1)

rest(5, "seconds. When the sound effect starts, you start. Prepare for Jumping Jacks.")
exercise(25, "seconds for Exercise 1: Jumping Jacks")
rest(10, "seconds left to rest. Next: Wall Sit.")
exercise(25, "seconds for Exercise 2: Wall Sit")
rest(10, "seconds left to rest. Next: Push-Ups.")
exercise(25, "seconds for Exercise 3: Push-Ups")
rest(10, "seconds left to rest. Next: Abdominal Crunches")
exercise(25, "seconds for Exercise 4: Abdominal Crunches")
rest(10, "seconds left to rest. Next: Step-Ups onto a Chair")
exercise(25, "seconds for Exercise 5: Step-Ups onto a Chair ")
rest(10, "seconds left to rest. Next: Squats")
exercise(25, "seconds for Exercise 6: Squats")
rest(10, "seconds left to rest. Next: Tricep Dips on a Chair")
exercise(25, "seconds for Exercise 7: Tricep Dips on a Chair")
rest(10, "seconds left to rest. Next: Plank")
exercise(25, "seconds for Exercise 8: Plank")
rest(10, "seconds left to rest. Next: High Knees Running")
exercise(25, "seconds for Exercise 9: High Knees")
rest(10, "seconds left to rest. Next: Lunges")
exercise(25, "seconds for Exercise 10: Lunges")
rest(10, "seconds left to rest. Next: Push-Up with Rotation")
exercise(25, "seconds for Exercise 11: Push-Up with Rotation")
rest(10, "seconds left to rest. Next: Side Plank")
exercise(25, "seconds for Exercise 12: Side Plank")

print("")
print("")
print("")
print("Well done!")
print("You've completed the 7-minute workout!")
print("")
