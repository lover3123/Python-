"""Chapter 6: Manipulating Strings
Section: The isX String Methods
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch6: strings, text editing
File: ch06_shell_18_the_isx_string_methods_hello_isalpha.py (18 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'hello'.isalpha()
# OUT: True
'hello123'.isalpha()
# OUT: False
'hello123'.isalnum()
# OUT: True
'hello'.isalnum()
# OUT: True
'123'.isdecimal()
# OUT: True
'    '.isspace()
# OUT: True
'This Is Title Case'.istitle()
# OUT: True
'This Is Title Case 123'.istitle()
# OUT: True
'This Is not Title Case'.istitle()
# OUT: False
'This Is NOT Title Case Either'.istitle()
# OUT: False
