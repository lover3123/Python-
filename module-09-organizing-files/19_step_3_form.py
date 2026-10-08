# Ch9 | 19/23 | Step 3: Form the New Filename and Rename the Files [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter9

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
