# Ch5 | 11/37 | Checking Whether a Key or Value Exists in a Dictionary [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter5

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys()
# OUT: True
'Zophie' in spam.values()
# OUT: True
'color' in spam.keys()
# OUT: False
'color' not in spam.keys()
# OUT: True
'color' in spam
# OUT: False
