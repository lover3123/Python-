# Ch4 | 44/62 | Sorting the Values in a List with the sort() Method [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam
# OUT: ['a', 'A', 'z', 'Z']
