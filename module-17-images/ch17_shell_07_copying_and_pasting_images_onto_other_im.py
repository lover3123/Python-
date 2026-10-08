"""Chapter 17: Manipulating Images
Section: Copying and Pasting Images onto Other Images
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter17
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch17: Pillow
File: ch17_shell_07_copying_and_pasting_images_onto_other_im.py (7 of 24 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()
