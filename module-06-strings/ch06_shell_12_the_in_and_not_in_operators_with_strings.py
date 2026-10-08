"""Chapter 6: Manipulating Strings
Section: The in and not in Operators with Strings
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch6: strings, text editing
File: ch06_shell_12_the_in_and_not_in_operators_with_strings.py (12 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'Hello' in 'Hello World'
# OUT: True
'Hello' in 'Hello'
# OUT: True
'HELLO' in 'Hello World'
# OUT: False
'' in 'spam'
# OUT: True
'cats' not in 'cats and dogs'
# OUT: False
