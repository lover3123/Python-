"""Chapter 9: Organizing Files
Section: Reading ZIP Files
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_shell_12_reading_zip_files_import_zipfile_os.py (12 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import zipfile, os
os.chdir('C:\\')    # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
# OUT:    ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
# OUT:    13908
spamInfo.compress_size
# OUT:    3828
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
# OUT:    .compress_size, 2))
# OUT:    'Compressed file is 3.63x smaller!'
exampleZip.close()
