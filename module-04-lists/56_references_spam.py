# Ch4 | 56/62 | References [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
spam
# OUT:    [0, 'Hello!', 2, 3, 4, 5]
cheese
# OUT:    [0, 'Hello!', 2, 3, 4, 5]
