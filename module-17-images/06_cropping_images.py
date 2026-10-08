# Ch17 | 06/24 | Cropping Images [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter17

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')
