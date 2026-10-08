# Ch4 | 38/62 | Removing Values from Lists with remove() [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('chicken')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#11>", line 1, in <module>
# OUT:     spam.remove('chicken')
# OUT: ValueError: list.remove(x): x not in list
