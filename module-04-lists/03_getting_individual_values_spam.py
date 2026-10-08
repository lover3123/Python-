# Ch4 | 03/62 | Getting Individual Values in a List with Indexes [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'bat', 'rat', 'elephant']
spam[10000]
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#9>", line 1, in <module>
# OUT:     spam[10000]
# OUT: IndexError: list index out of range
