"""Chapter 4: Lists
Section: Mutable and Immutable Data Types
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_47_mutable_and_immutable_data_types_name_zo.py (47 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

name = 'Zophie a cat'
name[7] = 'the'
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#50>", line 1, in <module>
# OUT:     name[7] = 'the'
# OUT: TypeError: 'str' object does not support item assignment
