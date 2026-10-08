"""Chapter 6: Manipulating Strings
Section: The join() and split() String Methods
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch6: strings, text editing
File: ch06_shell_24_the_join_and_split_string_methods_myabcn.py (24 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'MyABCnameABCisABCSimon'.split('ABC')
# OUT: ['My', 'name', 'is', 'Simon']
'My name is Simon'.split('m')
# OUT: ['My na', 'e is Si', 'on']
