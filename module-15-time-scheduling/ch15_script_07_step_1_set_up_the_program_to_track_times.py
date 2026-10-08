"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Step 1: Set Up the Program to Track Times
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: book script/example
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_script_07_step_1_set_up_the_program_to_track_times.py (7 of 37 in this chapter)
"""

#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.
Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times.
