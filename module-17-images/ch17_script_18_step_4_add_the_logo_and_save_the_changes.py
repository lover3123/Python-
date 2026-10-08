"""Chapter 17: Manipulating Images
Section: Step 4: Add the Logo and Save the Changes
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter17
Type: book script/example
PPT map: Syllabus Ch17: Pillow
File: ch17_script_18_step_4_add_the_logo_and_save_the_changes.py (18 of 24 in this chapter)
"""

   #! python3
   # resizeAndAddLogo.py - Resizes all images in current working directory to fit
   # in a 300x300 square, and adds catlogo.png to the lower-right corner.

   import os
   from PIL import Image

--snip--

    # Check if image needs to be resized.
    --snip--

    # Add the logo.
  print('Adding logo to %s...' % (filename))
  im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
  im.save(os.path.join('withLogo', filename))
