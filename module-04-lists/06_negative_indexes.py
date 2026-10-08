# Ch4 | 06/62 | Negative Indexes [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1]
# OUT: 'elephant'
spam[-3]
# OUT: 'bat'
'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
# OUT: 'The elephant is afraid of the bat.'
