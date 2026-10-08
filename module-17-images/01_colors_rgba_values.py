# Ch17 | 01/24 | Colors and RGBA Values [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter17

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

from PIL import ImageColor
ImageColor.getcolor('red', 'RGBA')
# OUT:    (255, 0, 0, 255)
ImageColor.getcolor('RED', 'RGBA')
# OUT:    (255, 0, 0, 255)
ImageColor.getcolor('Black', 'RGBA')
# OUT:    (0, 0, 0, 255)
ImageColor.getcolor('chocolate', 'RGBA')
# OUT:    (210, 105, 30, 255)
ImageColor.getcolor('CornflowerBlue', 'RGBA')
# OUT:    (100, 149, 237, 255)
