"""Chapter 17: Manipulating Images
Section: Step 3: Resize the Images
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter17
Type: book script/example
PPT map: Syllabus Ch17: Pillow
File: ch17_script_17_step_3_resize_the_images_python3.py (17 of 24 in this chapter)
"""

   #! python3
   # resizeAndAddLogo.py - Resizes all images in current working directory to fit
   # in a 300x300 square, and adds catlogo.png to the lower-right corner.

   import os
   from PIL import Image

   --snip--

      # Check if image needs to be resized.
      if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
          # Calculate the new width and height to resize to.
          if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
              width = SQUARE_FIT_SIZE
          else:
            width = int((SQUARE_FIT_SIZE / height) * width)
              height = SQUARE_FIT_SIZE

          # Resize the image.
          print('Resizing %s...' % (filename))
          im = im.resize((width, height))

--snip--
