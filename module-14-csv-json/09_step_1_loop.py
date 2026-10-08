# Ch14 | 09/21 | Step 1: Loop Through Each CSV File [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter14

   #! python3
   # removeCsvHeader.py - Removes the header from all CSV files in the current
   # working directory.

   import csv, os

   os.makedirs('headerRemoved', exist_ok=True)

   # Loop through every file in the current working directory.
   for csvFilename in os.listdir('.'):
       if not csvFilename.endswith('.csv'):
         continue    # skip non-csv files

       print('Removing header from ' + csvFilename + '...')

       # TODO: Read the CSV file in (skipping first row).

       # TODO: Write out the CSV file.
