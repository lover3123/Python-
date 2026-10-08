# Ch4 | 47/62 | Mutable and Immutable Data Types [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

name = 'Zophie a cat'
name[7] = 'the'
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#50>", line 1, in <module>
# OUT:     name[7] = 'the'
# OUT: TypeError: 'str' object does not support item assignment
