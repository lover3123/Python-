# Ch14 | 11/21 | Step 3: Write Out the CSV File Without the First Row [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter14

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
