# Ch9 | 17/23 | Step 2: Identify the Date Parts from the Filenames [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter9

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
