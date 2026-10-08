"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Launching Other Programs from Python
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_29_launching_other_programs_from_python_cal.py (29 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
calcProc.poll() == None
# OUT:    True
calcProc.wait()
# OUT:    0
calcProc.poll()
# OUT:    0
