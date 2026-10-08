"""Chapter 6: Manipulating Strings
Section: The upper(), lower(), isupper(), and islower() String Methods
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch6: strings, text editing
File: ch06_shell_16_the_upper_lower_isupper_and_islower_stri.py (16 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = 'Hello world!'
spam.islower()
# OUT: False
spam.isupper()
# OUT: False
'HELLO'.isupper()
# OUT: True
'abc12345'.islower()
# OUT: True
'12345'.islower()
# OUT: False
'12345'.isupper()
# OUT: False
