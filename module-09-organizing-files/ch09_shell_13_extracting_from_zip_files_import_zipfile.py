"""Chapter 9: Organizing Files
Section: Extracting from ZIP Files
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_shell_13_extracting_from_zip_files_import_zipfile.py (13 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import zipfile, os
os.chdir('C:\\')    # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()
