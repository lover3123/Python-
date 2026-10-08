# Ch17 | 17/24 | Step 3: Resize the Images [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter17

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
