"""Chapter 9: Organizing Files
Section: Extracting from ZIP Files
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_shell_14_extracting_from_zip_files_examplezip_ext.py (14 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

exampleZip.extract('spam.txt')
# OUT: 'C:\\spam.txt'
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
# OUT: 'C:\\some\\new\\folders\\spam.txt'
exampleZip.close()
