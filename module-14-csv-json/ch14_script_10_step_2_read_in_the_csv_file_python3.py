"""Chapter 14: CSV Files and JSON Data
Section: Step 2: Read in the CSV File
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter14
Type: book script/example
PPT map: Syllabus Ch14: csv, json
File: ch14_script_10_step_2_read_in_the_csv_file_python3.py (10 of 21 in this chapter)
"""

#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.

--snip--
# Read the CSV file in (skipping first row).
csvRows = []
csvFileObj = open(csvFilename)
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue    # skip first row
    csvRows.append(row)
csvFileObj.close()

# TODO: Write out the CSV file.
