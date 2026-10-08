# Ch4 | 52/62 | The Tuple Data Type [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

eggs = ('hello', 42, 0.5)
eggs[1] = 99
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#5>", line 1, in <module>
# OUT:     eggs[1] = 99
# OUT: TypeError: 'tuple' object does not support item assignment
