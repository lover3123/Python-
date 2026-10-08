# Ch17 | 14/24 | Changing Individual Pixels [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter17

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

im = Image.new('RGBA', (100, 100))
im.getpixel((0, 0))
# OUT:    (0, 0, 0, 0)
for x in range(100):
# OUT:            for y in range(50):
# OUT:              im.putpixel((x, y), (210, 210, 210))
from PIL import ImageColor
for x in range(100):
# OUT:            for y in range(50, 100):
# OUT:              im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
im.getpixel((0, 0))
# OUT:    (210, 210, 210, 255)
im.getpixel((0, 50))
# OUT:    (169, 169, 169, 255)
im.save('putPixel.png')
