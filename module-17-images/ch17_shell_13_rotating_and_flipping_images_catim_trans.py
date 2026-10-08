"""Chapter 17: Manipulating Images
Section: Rotating and Flipping Images
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter17
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch17: Pillow
File: ch17_shell_13_rotating_and_flipping_images_catim_trans.py (13 of 24 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')
