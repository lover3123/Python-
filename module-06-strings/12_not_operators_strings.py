# Ch6 | 12/46 | The in and not in Operators with Strings [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter6

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'Hello' in 'Hello World'
# OUT: True
'Hello' in 'Hello'
# OUT: True
'HELLO' in 'Hello World'
# OUT: False
'' in 'spam'
# OUT: True
'cats' not in 'cats and dogs'
# OUT: False
