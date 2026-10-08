# Ch6 | 18/46 | The isX String Methods [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter6

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'hello'.isalpha()
# OUT: True
'hello123'.isalpha()
# OUT: False
'hello123'.isalnum()
# OUT: True
'hello'.isalnum()
# OUT: True
'123'.isdecimal()
# OUT: True
'    '.isspace()
# OUT: True
'This Is Title Case'.istitle()
# OUT: True
'This Is Title Case 123'.istitle()
# OUT: True
'This Is not Title Case'.istitle()
# OUT: False
'This Is NOT Title Case Either'.istitle()
# OUT: False
