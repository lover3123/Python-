"""Chapter 1: Python Basics
Section: The str(), int(), and float() Functions
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter1
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-1: intro, expressions, datatypes, variables, print/input/len/str-int-float, operators
File: ch01_shell_28_the_str_int_and_float_functions_int_99_9.py (28 of 30 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

int('99.99')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#18>", line 1, in <module>
# OUT:     int('99.99')
# OUT: ValueError: invalid literal for int() with base 10: '99.99'
int('twelve')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#19>", line 1, in <module>
# OUT:     int('twelve')
# OUT: ValueError: invalid literal for int() with base 10: 'twelve'
