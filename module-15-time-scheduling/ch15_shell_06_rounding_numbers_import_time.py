"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Rounding Numbers
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_06_rounding_numbers_import_time.py (6 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import time
now = time.time()
now
# OUT: 1425064108.017826
round(now, 2)
# OUT: 1425064108.02
round(now, 4)
# OUT: 1425064108.0178
round(now)
# OUT: 1425064108
