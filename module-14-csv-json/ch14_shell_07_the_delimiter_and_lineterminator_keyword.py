"""Chapter 14: CSV Files and JSON Data
Section: The delimiter and lineterminator Keyword Arguments
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter14
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch14: csv, json
File: ch14_shell_07_the_delimiter_and_lineterminator_keyword.py (7 of 21 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import csv
csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
# OUT:    24
csvWriter.writerow(['eggs', 'bacon', 'ham'])
# OUT:    17
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
# OUT:    32
csvFile.close()
