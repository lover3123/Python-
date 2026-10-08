# Ch6 | 17/46 | The upper(), lower(), isupper(), and islower() String Methods [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter6

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'Hello'.upper()
# OUT: 'HELLO'
'Hello'.upper().lower()
# OUT: 'hello'
'Hello'.upper().lower().upper()
# OUT: 'HELLO'
'HELLO'.lower()
# OUT: 'hello'
'HELLO'.lower().islower()
# OUT: True
