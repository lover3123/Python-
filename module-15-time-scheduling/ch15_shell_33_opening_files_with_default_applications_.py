"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Opening Files with Default Applications
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_shell_33_opening_files_with_default_applications_.py (33 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

subprocess.Popen(['open', '/Applications/Calculator.app/'])
# OUT: <subprocess.Popen object at 0x10202ff98>
