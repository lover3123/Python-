"""Chapter 1: Python Basics
Section: String Concatenation and Replication
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter1
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-1: intro, expressions, datatypes, variables, print/input/len/str-int-float, operators
File: ch01_shell_10_string_concatenation_and_replication_ali.py (10 of 30 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'Alice' * 'Bob'
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#32>", line 1, in <module>
# OUT:     'Alice' * 'Bob'
# OUT: TypeError: can't multiply sequence by non-int of type 'str'
'Alice' * 5.0
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#33>", line 1, in <module>
# OUT:     'Alice' * 5.0
# OUT: TypeError: can't multiply sequence by non-int of type 'float'
