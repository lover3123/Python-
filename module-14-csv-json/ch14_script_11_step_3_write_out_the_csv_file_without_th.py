"""Chapter 14: CSV Files and JSON Data
Section: Step 3: Write Out the CSV File Without the First Row
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter14
Type: book script/example
PPT map: Syllabus Ch14: csv, json
File: ch14_script_11_step_3_write_out_the_csv_file_without_th.py (11 of 21 in this chapter)
"""

   #! python3
   # removeCsvHeader.py - Removes the header from all CSV files in the current
   # working directory.
   --snip--

   # Loop through every file in the current working directory.
 for csvFilename in os.listdir('.'):
       if not csvFilename.endswith('.csv'):
           continue    # skip non-CSV files

       --snip--

       # Write out the CSV file.
       csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',
                    newline='')
       csvWriter = csv.writer(csvFileObj)
       for row in csvRows:
           csvWriter.writerow(row)
       csvFileObj.close()
