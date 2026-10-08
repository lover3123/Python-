"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: The datetime Module
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_09_the_datetime_module_import_datetime.py (9 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import datetime
datetime.datetime.now()
# OUT:  datetime.datetime(2015, 2, 27, 11, 10, 49, 55, 53)
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
dt.year, dt.month, dt.day
# OUT:    (2015, 10, 21)
dt.hour, dt.minute, dt.second
# OUT:    (16, 29, 0)
