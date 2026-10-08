"""Chapter 4: Lists
Section: Mutable and Immutable Data Types
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_48_mutable_and_immutable_data_types_name_zo.py (48 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
name
# OUT: 'Zophie a cat'
newName
# OUT: 'Zophie the cat'
