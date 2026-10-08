# Ch6 | 21/46 | The startswith() and endswith() String Methods [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter6

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'Hello world!'.startswith('Hello')
# OUT: True
'Hello world!'.endswith('world!')
# OUT: True
'abc123'.startswith('abcdef')
# OUT: False
'abc123'.endswith('12')
# OUT: False
'Hello world!'.startswith('Hello world!')
# OUT: True
'Hello world!'.endswith('Hello world!')
# OUT: True
