"""Chapter 6: Manipulating Strings
Section: Copying and Pasting Strings with the pyperclip Module
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch6: strings, text editing
File: ch06_shell_33_copying_and_pasting_strings_with_the_pyp.py (33 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()
# OUT: 'Hello world!'
