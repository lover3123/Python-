# Ch14 | 07/21 | The delimiter and lineterminator Keyword Arguments [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter14

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
