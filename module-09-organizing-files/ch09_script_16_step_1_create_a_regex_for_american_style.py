"""Chapter 9: Organizing Files
Section: Step 1: Create a Regex for American-Style Dates
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: book script/example
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_script_16_step_1_create_a_regex_for_american_style.py (16 of 23 in this chapter)
"""

   #! python3
   # renameDates.py - Renames filenames with American MM-DD-YYYY date format
   # to European DD-MM-YYYY.

 import shutil, os, re

   # Create a regex that matches files with the American date format.
 datePattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
     """, re.VERBOSE)

   # TODO: Loop over the files in the working directory.

   # TODO: Skip files without a date.

   # TODO: Get the different parts of the filename.

   # TODO: Form the European-style filename.

   # TODO: Get the full, absolute file paths.

   # TODO: Rename the files.
