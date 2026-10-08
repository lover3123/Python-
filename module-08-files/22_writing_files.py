# Ch8 | 22/40 | Writing to Files [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
# OUT: 13
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
# OUT: 25
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
# OUT: Hello world!
# OUT: Bacon is not a vegetable.
