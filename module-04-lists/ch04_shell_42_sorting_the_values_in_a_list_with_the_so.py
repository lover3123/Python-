"""Chapter 4: Lists
Section: Sorting the Values in a List with the sort() Method
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_42_sorting_the_values_in_a_list_with_the_so.py (42 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort()
# OUT: Traceback (most recent call last):
# OUT:  File "<pyshell#70>", line 1, in <module>
# OUT:    spam.sort()
# OUT: TypeError: unorderable types: str() < int()
