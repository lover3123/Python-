"""Chapter 4: Lists
Section: Adding Values to Lists with the append() and insert() Methods
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_35_adding_values_to_lists_with_the_append_a.py (35 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam
# OUT: ['cat', 'chicken', 'dog', 'bat']
