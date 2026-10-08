"""Chapter 4: Lists
Section: Sorting the Values in a List with the sort() Method
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_40_sorting_the_values_in_a_list_with_the_so.py (40 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam
# OUT: [-7, 1, 2, 3.14, 5]
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam
# OUT: ['ants', 'badgers', 'cats', 'dogs', 'elephants']
