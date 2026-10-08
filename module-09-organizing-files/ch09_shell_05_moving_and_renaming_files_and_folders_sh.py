"""Chapter 9: Organizing Files
Section: Moving and Renaming Files and Folders
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_shell_05_moving_and_renaming_files_and_folders_sh.py (5 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

shutil.move('C:\\bacon.txt', 'C:\\eggs')
# OUT: 'C:\\eggs'
