"""Chapter 17: Manipulating Images
Section: Drawing Shapes
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter17
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch17: Pillow
File: ch17_shell_21_drawing_shapes_from_pil_import_image_ima.py (21 of 24 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

from PIL import Image, ImageDraw
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),
# OUT:    fill='brown')
for i in range(100, 200, 10):
# OUT:            draw.line([(i, 0), (200, i - 100)], fill='green')

im.save('drawing.png')
