# Ch9 | 14/23 | Extracting from ZIP Files [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter9

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

exampleZip.extract('spam.txt')
# OUT: 'C:\\spam.txt'
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
# OUT: 'C:\\some\\new\\folders\\spam.txt'
exampleZip.close()
