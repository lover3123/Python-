"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: The timedelta Data Type
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_12_the_timedelta_data_type_delta_datetime_t.py (12 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
# OUT:    (11, 36548, 0)
delta.total_seconds()
# OUT:    986948.0
str(delta)
# OUT:    '11 days, 10:09:08'
