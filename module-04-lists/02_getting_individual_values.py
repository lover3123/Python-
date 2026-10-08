# Ch4 | 02/62 | Getting Individual Values in a List with Indexes [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

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
