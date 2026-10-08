"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Converting datetime Objects into Strings
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_16_converting_datetime_objects_into_strings.py (16 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
# OUT: '2015/10/21 16:29:00'
oct21st.strftime('%I:%M %p')
# OUT: '04:29 PM'
oct21st.strftime("%B of '%y")
# OUT: "October of '15"
