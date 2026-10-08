"""Chapter 14: CSV Files and JSON Data
Section: Step 1: Loop Through Each CSV File
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter14
Type: book script/example
PPT map: Syllabus Ch14: csv, json
File: ch14_script_09_step_1_loop_through_each_csv_file_python.py (9 of 21 in this chapter)
"""

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
