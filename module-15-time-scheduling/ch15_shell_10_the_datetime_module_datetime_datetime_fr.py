"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: The datetime Module
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_10_the_datetime_module_datetime_datetime_fr.py (10 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

datetime.datetime.fromtimestamp(1000000)
# OUT: datetime.datetime(1970, 1, 12, 5, 46, 40)
datetime.datetime.fromtimestamp(time.time())
# OUT: datetime.datetime(2015, 2, 27, 11, 13, 0, 604980)
