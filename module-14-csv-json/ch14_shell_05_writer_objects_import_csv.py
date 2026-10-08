"""Chapter 14: CSV Files and JSON Data
Section: Writer Objects
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter14
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch14: csv, json
File: ch14_shell_05_writer_objects_import_csv.py (5 of 21 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# OUT:    21
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# OUT:    32
outputWriter.writerow([1, 2, 3.141592, 4])
# OUT:    16
outputFile.close()
