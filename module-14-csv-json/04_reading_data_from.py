# Ch14 | 04/21 | Reading Data from Reader Objects in a for Loop [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter14

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
