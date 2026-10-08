"""Chapter 9: Organizing Files
Section: Step 2: Create the New ZIP File
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: book script/example
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_script_21_step_2_create_the_new_zip_file_python3.py (21 of 23 in this chapter)
"""

   #! python3
   # backupToZip.py - Copies an entire folder and its contents into
   # a ZIP file whose filename increments.

   --snip--
       while True:
           zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
           if not os.path.exists(zipFilename):
               break
           number = number + 1

       # Create the ZIP file.
       print('Creating %s...' % (zipFilename))
     backupZip = zipfile.ZipFile(zipFilename, 'w')

       # TODO: Walk the entire folder tree and compress the files in each folder.
       print('Done.')

   backupToZip('C:\\delicious')
