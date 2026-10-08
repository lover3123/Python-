"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Step 1: Count Down
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: book script/example
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_script_34_step_1_count_down_python3.py (34 of 37 in this chapter)
"""

   #! python3
   # countdown.py - A simple countdown script.

   import time, subprocess

 timeLeft = 60
   while timeLeft > 0:
     print(timeLeft, end='')
     time.sleep(1)
     timeLeft = timeLeft - 1

   # TODO: At the end of the countdown, play a sound file.
