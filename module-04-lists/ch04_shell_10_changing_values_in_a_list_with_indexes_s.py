"""Chapter 4: Lists
Section: Changing Values in a List with Indexes
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_10_changing_values_in_a_list_with_indexes_s.py (10 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
spam
# OUT: ['cat', 'aardvark', 'rat', 'elephant']
spam[2] = spam[1]
spam
# OUT: ['cat', 'aardvark', 'aardvark', 'elephant']
spam[-1] = 12345
spam
# OUT: ['cat', 'aardvark', 'aardvark', 12345]
