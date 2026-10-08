"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Launching Other Programs from Python
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_27_launching_other_programs_from_python_imp.py (27 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import subprocess
subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# OUT: <subprocess.Popen object at 0x0000000003055A58>
