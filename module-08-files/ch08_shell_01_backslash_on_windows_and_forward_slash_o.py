"""Chapter 8: Reading and Writing Files
Section: Backslash on Windows and Forward Slash on OS X and Linux
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_01_backslash_on_windows_and_forward_slash_o.py (1 of 40 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import os
os.path.join('usr', 'bin', 'spam')
# OUT: 'usr\\bin\\spam'
