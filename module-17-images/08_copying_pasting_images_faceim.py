# Ch17 | 08/24 | Copying and Pasting Images onto Other Images [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter17

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

faceIm = catIm.crop((335, 345, 565, 560))
faceIm.size
# OUT: (230, 215)
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted.png')
