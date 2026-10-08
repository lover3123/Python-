"""Chapter 17: Manipulating Images
Section: Colors and RGBA Values
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter17
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch17: Pillow
File: ch17_shell_01_colors_and_rgba_values_from_pil_import_i.py (1 of 24 in this chapter)
"""

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
