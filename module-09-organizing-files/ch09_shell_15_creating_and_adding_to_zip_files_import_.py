"""Chapter 9: Organizing Files
Section: Creating and Adding to ZIP Files
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_shell_15_creating_and_adding_to_zip_files_import_.py (15 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
