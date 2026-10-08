"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: The timedelta Data Type
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_14_the_timedelta_data_type_oct21st_datetime.py (14 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
oct21st
# OUT:    datetime.datetime(2015, 10, 21, 16, 29)
oct21st - aboutThirtyYears
# OUT:    datetime.datetime(1985, 10, 28, 16, 29)
oct21st - (2 * aboutThirtyYears)
# OUT:    datetime.datetime(1955, 11, 5, 16, 29)
