"""Chapter 6: Manipulating Strings
Section: The startswith() and endswith() String Methods
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch6: strings, text editing
File: ch06_shell_21_the_startswith_and_endswith_string_metho.py (21 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'Hello world!'.startswith('Hello')
# OUT: True
'Hello world!'.endswith('world!')
# OUT: True
'abc123'.startswith('abcdef')
# OUT: False
'abc123'.endswith('12')
# OUT: False
'Hello world!'.startswith('Hello world!')
# OUT: True
'Hello world!'.endswith('Hello world!')
# OUT: True
