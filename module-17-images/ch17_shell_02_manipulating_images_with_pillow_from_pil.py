"""Chapter 17: Manipulating Images
Section: Manipulating Images with Pillow
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter17
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch17: Pillow
File: ch17_shell_02_manipulating_images_with_pillow_from_pil.py (2 of 24 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

from PIL import Image
catIm = Image.open('zophie.png')
