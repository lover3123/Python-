"""Chapter 9: Organizing Files
Section: Step 1: Figure Out the ZIP File’s Name
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: book script/example
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_script_20_step_1_figure_out_the_zip_file_s_name_py.py (20 of 23 in this chapter)
"""

   #! python3
   # backupToZip.py - Copies an entire folder and its contents into
   # a ZIP file whose filename increments.

 import zipfile, os

   def backupToZip(folder):
       # Backup the entire contents of "folder" into a ZIP file.

       folder = os.path.abspath(folder) # make sure folder is absolute

       # Figure out the filename this code should use based on
       # what files already exist.
     number = 1
     while True:
           zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
           if not os.path.exists(zipFilename):
               break
           number = number + 1

     # TODO: Create the ZIP file.

       # TODO: Walk the entire folder tree and compress the files in each folder.
       print('Done.')

   backupToZip('C:\\delicious')
