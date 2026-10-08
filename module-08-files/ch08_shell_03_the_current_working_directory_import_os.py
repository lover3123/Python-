"""Chapter 8: Reading and Writing Files
Section: The Current Working Directory
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_03_the_current_working_directory_import_os.py (3 of 40 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import os
os.getcwd()
# OUT: 'C:\\Python34'
os.chdir('C:\\Windows\\System32')
os.getcwd()
# OUT: 'C:\\Windows\\System32'
