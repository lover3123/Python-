"""Chapter 6: Manipulating Strings
Section: Step 3: Join the Modified Lines
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: book script/example
PPT map: Syllabus Ch6: strings, text editing
File: ch06_script_44_step_3_join_the_modified_lines_python3.py (44 of 46 in this chapter)
"""

#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
