"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Converting Strings into datetime Objects
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_17_converting_strings_into_datetime_objects.py (17 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
# OUT:    datetime.datetime(2015, 10, 21, 0, 0)
datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
# OUT:    datetime.datetime(2015, 10, 21, 16, 29)
datetime.datetime.strptime("October of '15", "%B of '%y")
# OUT:    datetime.datetime(2015, 10, 1, 0, 0)
datetime.datetime.strptime("November of '63", "%B of '%y")
# OUT:    datetime.datetime(2063, 11, 1, 0, 0)
