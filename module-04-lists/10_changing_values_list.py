# Ch4 | 10/62 | Changing Values in a List with Indexes [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
spam
# OUT: ['cat', 'aardvark', 'rat', 'elephant']
spam[2] = spam[1]
spam
# OUT: ['cat', 'aardvark', 'aardvark', 'elephant']
spam[-1] = 12345
spam
# OUT: ['cat', 'aardvark', 'aardvark', 12345]
