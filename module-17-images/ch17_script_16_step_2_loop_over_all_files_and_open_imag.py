"""Chapter 17: Manipulating Images
Section: Step 2: Loop Over All Files and Open Images
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter17
Type: book script/example
PPT map: Syllabus Ch17: Pillow
File: ch17_script_16_step_2_loop_over_all_files_and_open_imag.py (16 of 24 in this chapter)
"""

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
