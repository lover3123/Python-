"""Chapter 9: Organizing Files
Section: Step 3: Walk the Directory Tree and Add to the ZIP File
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: book script/example
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_script_22_step_3_walk_the_directory_tree_and_add_t.py (22 of 23 in this chapter)
"""

   #! python3
   # backupToZip.py - Copies an entire folder and its contents into
   # a ZIP file whose filename increments.

   --snip--

       # Walk the entire folder tree and compress the files in each folder.
     for foldername, subfolders, filenames in os.walk(folder):
           print('Adding files in %s...' % (foldername))
           # Add the current folder to the ZIP file.
         backupZip.write(foldername)
           # Add all the files in this folder to the ZIP file.
         for filename in filenames:
               newBase = os.path.basename(folder) + '_'
               if filename.startswith(newBase) and filename.endswith('.zip'):
                   continue   # don't backup the backup ZIP files
               backupZip.write(os.path.join(foldername, filename))
       backupZip.close()
       print('Done.')


   backupToZip('C:\\delicious')
