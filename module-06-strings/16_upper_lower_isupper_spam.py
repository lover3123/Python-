# Ch6 | 16/46 | The upper(), lower(), isupper(), and islower() String Methods [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter6

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = 'Hello world!'
spam.islower()
# OUT: False
spam.isupper()
# OUT: False
'HELLO'.isupper()
# OUT: True
'abc12345'.islower()
# OUT: True
'12345'.islower()
# OUT: False
'12345'.isupper()
# OUT: False
