"""Chapter 6: Manipulating Strings
Section: Step 1: Copy and Paste from the Clipboard
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: book script/example
PPT map: Syllabus Ch6: strings, text editing
File: ch06_script_41_step_1_copy_and_paste_from_the_clipboard.py (41 of 46 in this chapter)
"""

#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars.

pyperclip.copy(text)
