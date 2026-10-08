# Ch17 | 15/24 | Step 1: Open the Logo Image [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter17

   #! python3
   # resizeAndAddLogo.py - Resizes all images in current working directory to fit
   # in a 300x300 square, and adds catlogo.png to the lower-right corner.
   import os
   from PIL import Image

 SQUARE_FIT_SIZE = 300
 LOGO_FILENAME = 'catlogo.png'

 logoIm = Image.open(LOGO_FILENAME)
 logoWidth, logoHeight = logoIm.size

   # TODO: Loop over all files in the working directory.

   # TODO: Check if image needs to be resized.

   # TODO: Calculate the new width and height to resize to.

   # TODO: Resize the image.

   # TODO: Add the logo.

   # TODO: Save changes.
