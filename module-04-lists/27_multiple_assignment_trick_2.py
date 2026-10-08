# Ch4 | 27/62 | The Multiple Assignment Trick [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

a, b = 'Alice', 'Bob'
a, b = b, a
print(a)
# OUT: 'Bob'
print(b)
# OUT: 'Alice'
