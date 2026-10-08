"""Chapter 9: Organizing Files
Section: Safe Deletes with the send2trash Module
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_shell_09_safe_deletes_with_the_send2trash_module_.py (9 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import send2trash
baconFile = open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')
# OUT: 25
baconFile.close()
send2trash.send2trash('bacon.txt')
