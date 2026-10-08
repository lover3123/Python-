# Ch9 | 21/23 | Step 2: Create the New ZIP File [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter9

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
