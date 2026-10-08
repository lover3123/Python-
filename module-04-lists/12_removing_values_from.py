# Ch4 | 12/62 | Removing Values from Lists with del Statements [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
spam
# OUT: ['cat', 'bat', 'elephant']
del spam[2]
spam
# OUT: ['cat', 'bat']
