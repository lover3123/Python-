"""Chapter 4: Lists
Section: Getting Sublists with Slices
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_08_getting_sublists_with_slices_spam_cat_ba.py (8 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2]
# OUT: ['cat', 'bat']
spam[1:]
# OUT: ['bat', 'rat', 'elephant']
spam[:]
# OUT: ['cat', 'bat', 'rat', 'elephant']
