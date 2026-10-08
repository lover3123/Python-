"""Chapter 4: Lists
Section: The in and not in Operators
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_21_the_in_and_not_in_operators_howdy_in_hel.py (21 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'howdy' in ['hello', 'hi', 'howdy', 'heyas']
# OUT: True
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam
# OUT: False
'howdy' not in spam
# OUT: False
'cat' not in spam
# OUT: True
