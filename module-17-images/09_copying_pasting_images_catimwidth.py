# Ch17 | 09/24 | Copying and Pasting Images onto Other Images [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter17

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
# OUT:          for top in range(0, catImHeight, faceImHeight):
# OUT:                print(left, top)
# OUT:                catCopyTwo.paste(faceIm, (left, top))
# OUT:    0 0
# OUT:    0 215
# OUT:    0 430
# OUT:    0 645
# OUT:    0 860
# OUT:    0 1075
# OUT:    230 0
# OUT:    230 215
# OUT:    --snip--
# OUT:    690 860
# OUT:    690 1075
catCopyTwo.save('tiled.png')
