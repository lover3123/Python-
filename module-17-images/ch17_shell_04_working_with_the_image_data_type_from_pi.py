"""Chapter 17: Manipulating Images
Section: Working with the Image Data Type
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter17
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch17: Pillow
File: ch17_shell_04_working_with_the_image_data_type_from_pi.py (4 of 24 in this chapter)
"""

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
