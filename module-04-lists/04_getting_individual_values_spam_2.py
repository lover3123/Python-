# Ch4 | 04/62 | Getting Individual Values in a List with Indexes [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1]
# OUT: 'bat'
spam[1.0]
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#13>", line 1, in <module>
# OUT:     spam[1.0]
# OUT: TypeError: list indices must be integers, not float
spam[int(1.0)]
# OUT: 'bat'
