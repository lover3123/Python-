# Ch8 | 24/40 | Saving Variables with the shelve Module [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

shelfFile = shelve.open('mydata')
type(shelfFile)
# OUT: <class 'shelve.DbfilenameShelf'>
shelfFile['cats']
# OUT: ['Zophie', 'Pooka', 'Simon']
shelfFile.close()
