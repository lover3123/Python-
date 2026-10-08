"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: The timedelta Data Type
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_13_the_timedelta_data_type_dt_datetime_date.py (13 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

dt = datetime.datetime.now()
dt
# OUT: datetime.datetime(2015, 2, 27, 18, 38, 50, 636181)
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays
# OUT: datetime.datetime(2017, 11, 23, 18, 38, 50, 636181)
