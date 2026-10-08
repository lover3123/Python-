"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: The datetime Module
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_11_the_datetime_module_halloween2015_dateti.py (11 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
halloween2015 == oct31_2015
# OUT:    True
halloween2015 > newyears2016
# OUT:    False
newyears2016 > halloween2015
# OUT:    True
newyears2016 != oct31_2015
# OUT:    True
