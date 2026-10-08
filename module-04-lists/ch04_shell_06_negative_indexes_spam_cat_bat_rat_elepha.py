"""Chapter 4: Lists
Section: Negative Indexes
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_06_negative_indexes_spam_cat_bat_rat_elepha.py (6 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1]
# OUT: 'elephant'
spam[-3]
# OUT: 'bat'
'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
# OUT: 'The elephant is afraid of the bat.'
