"""Chapter 9: Organizing Files
Section: Permanently Deleting Files and Folders
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: book script/example
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_script_08_permanently_deleting_files_and_folders_i.py (8 of 23 in this chapter)
"""

import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)
