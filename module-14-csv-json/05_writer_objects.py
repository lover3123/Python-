# Ch14 | 05/21 | Writer Objects [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter14

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
