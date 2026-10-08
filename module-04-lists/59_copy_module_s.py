# Ch4 | 59/62 | The copy Module’s copy() and deepcopy() Functions [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
spam
# OUT: ['A', 'B', 'C', 'D']
cheese
# OUT: ['A', 42, 'C', 'D']
