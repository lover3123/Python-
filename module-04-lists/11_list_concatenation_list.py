# Ch4 | 11/62 | List Concatenation and List Replication [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

[1, 2, 3] + ['A', 'B', 'C']
# OUT: [1, 2, 3, 'A', 'B', 'C']
['X', 'Y', 'Z'] * 3
# OUT: ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
spam
# OUT: [1, 2, 3, 'A', 'B', 'C']
