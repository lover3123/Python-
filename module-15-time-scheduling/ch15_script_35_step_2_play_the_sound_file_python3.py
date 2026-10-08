"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Step 2: Play the Sound File
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: book script/example
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_script_35_step_2_play_the_sound_file_python3.py (35 of 37 in this chapter)
"""

#! python3
# countdown.py - A simple countdown script.

import time, subprocess

--snip--

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)
