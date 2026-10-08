"""Chapter 17: Manipulating Images
Section: Changing Individual Pixels
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter17
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch17: Pillow
File: ch17_shell_14_changing_individual_pixels_im_image_new_.py (14 of 24 in this chapter)
"""

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
