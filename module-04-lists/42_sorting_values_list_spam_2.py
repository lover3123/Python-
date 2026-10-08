# Ch4 | 42/62 | Sorting the Values in a List with the sort() Method [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort()
# OUT: Traceback (most recent call last):
# OUT:  File "<pyshell#70>", line 1, in <module>
# OUT:    spam.sort()
# OUT: TypeError: unorderable types: str() < int()
