# Ch17 | 04/24 | Working with the Image Data Type [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter17

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

from PIL import Image
catIm = Image.open('zophie.png')
catIm.size
# OUT:  (816, 1088)
width, height = catIm.size
width
# OUT:    816
height
# OUT:    1088
catIm.filename
# OUT:    'zophie.png'
catIm.format
# OUT:    'PNG'
catIm.format_description
# OUT:    'Portable network graphics'
catIm.save('zophie.jpg')
