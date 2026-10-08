"""Chapter 14: CSV Files and JSON Data
Section: Reading Data from Reader Objects in a for Loop
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter14
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch14: csv, json
File: ch14_shell_04_reading_data_from_reader_objects_in_a_fo.py (4 of 21 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
# OUT:         print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

# OUT: Row #1 ['4/5/2015 13:34', 'Apples', '73']
# OUT: Row #2 ['4/5/2015 3:41', 'Cherries', '85']
# OUT: Row #3 ['4/6/2015 12:46', 'Pears', '14']
# OUT: Row #4 ['4/8/2015 8:59', 'Oranges', '52']
# OUT: Row #5 ['4/10/2015 2:07', 'Apples', '152']
# OUT: Row #6 ['4/10/2015 18:10', 'Bananas', '23']
# OUT: Row #7 ['4/10/2015 2:40', 'Strawberries', '98']
