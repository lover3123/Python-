"""Chapter 17: Manipulating Images
Section: Cropping Images
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter17
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch17: Pillow
File: ch17_shell_06_cropping_images_croppedim_catim_crop_335.py (6 of 24 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')
