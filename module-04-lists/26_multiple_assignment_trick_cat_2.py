# Ch4 | 26/62 | The Multiple Assignment Trick [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

cat = ['fat', 'orange', 'loud']
size, color, disposition, name = cat
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#84>", line 1, in <module>
# OUT:     size, color, disposition, name = cat
# OUT: ValueError: need more than 3 values to unpack
