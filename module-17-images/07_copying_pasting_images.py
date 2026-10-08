# Ch17 | 07/24 | Copying and Pasting Images onto Other Images [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter17

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()
