"""Chapter 9: Organizing Files
Section: Step 2: Identify the Date Parts from the Filenames
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: book script/example
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_script_17_step_2_identify_the_date_parts_from_the_.py (17 of 23 in this chapter)
"""

   #! python3
   # renameDates.py - Renames filenames with American MM-DD-YYYY date format
   # to European DD-MM-YYYY.

   --snip--

   # Loop over the files in the working directory.
   for amerFilename in os.listdir('.'):
       mo = datePattern.search(amerFilename)

       # Skip files without a date.
     if mo == None:
         continue

     # Get the different parts of the filename.
       beforePart = mo.group(1)
       monthPart  = mo.group(2)
       dayPart    = mo.group(4)
       yearPart   = mo.group(6)
       afterPart  = mo.group(8)

   --snip--
