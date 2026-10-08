"""Chapter 4: Lists
Section: Getting Individual Values in a List with Indexes
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_02_getting_individual_values_in_a_list_with.py (2 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
# OUT:    'cat'
spam[1]
# OUT:    'bat'
spam[2]
# OUT:    'rat'
spam[3]
# OUT:    'elephant'
['cat', 'bat', 'rat', 'elephant'][3]
# OUT:    'elephant'
'Hello ' + spam[0]
# OUT:  'Hello cat'
'The ' + spam[1] + ' ate the ' + spam[0] + '.'
# OUT:    'The bat ate the cat.'
