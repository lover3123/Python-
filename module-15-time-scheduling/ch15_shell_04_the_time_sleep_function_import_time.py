"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: The time.sleep() Function
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_04_the_time_sleep_function_import_time.py (4 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import time
for i in range(3):
# OUT:          print('Tick')
# OUT:          time.sleep(1)
# OUT:          print('Tock')
# OUT:          time.sleep(1)
# OUT:    Tick
# OUT:    Tock
# OUT:    Tick
# OUT:    Tock
# OUT:    Tick
# OUT:    Tock
time.sleep(5)
