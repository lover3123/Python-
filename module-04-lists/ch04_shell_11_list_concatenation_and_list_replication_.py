"""Chapter 4: Lists
Section: List Concatenation and List Replication
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_11_list_concatenation_and_list_replication_.py (11 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

[1, 2, 3] + ['A', 'B', 'C']
# OUT: [1, 2, 3, 'A', 'B', 'C']
['X', 'Y', 'Z'] * 3
# OUT: ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
spam
# OUT: [1, 2, 3, 'A', 'B', 'C']
