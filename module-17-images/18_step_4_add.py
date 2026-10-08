# Ch17 | 18/24 | Step 4: Add the Logo and Save the Changes [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter17

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
