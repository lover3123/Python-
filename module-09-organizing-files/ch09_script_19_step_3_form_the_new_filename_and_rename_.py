"""Chapter 9: Organizing Files
Section: Step 3: Form the New Filename and Rename the Files
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: book script/example
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_script_19_step_3_form_the_new_filename_and_rename_.py (19 of 23 in this chapter)
"""

   #! python3
   # renameDates.py - Renames filenames with American MM-DD-YYYY date format
   # to European DD-MM-YYYY.

   --snip--

       # Form the European-style filename.
     euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart +
                      afterPart

       # Get the full, absolute file paths.
       absWorkingDir = os.path.abspath('.')
       amerFilename = os.path.join(absWorkingDir, amerFilename)
       euroFilename = os.path.join(absWorkingDir, euroFilename)

       # Rename the files.
     print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
     #shutil.move(amerFilename, euroFilename)   # uncomment after testing
