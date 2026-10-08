# Ch17 | 16/24 | Step 2: Loop Over All Files and Open Images [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter17

   #! python3
   # resizeAndAddLogo.py - Resizes all images in current working directory to fit
   # in a 300x300 square, and adds catlogo.png to the lower-right corner.

   import os
   from PIL import Image

   --snip--

   os.makedirs('withLogo', exist_ok=True)
   # Loop over all files in the working directory.
 for filename in os.listdir('.'):
     if not (filename.endswith('.png') or filename.endswith('.jpg')) \
          or filename == LOGO_FILENAME:
         continue # skip non-image files and the logo file itself

     im = Image.open(filename)
       width, height = im.size
   --snip--
