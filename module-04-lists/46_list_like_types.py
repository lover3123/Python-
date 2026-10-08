# Ch4 | 46/62 | List-like Types: Strings and Tuples [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

name = 'Zophie'
name[0]
# OUT: 'Z'
name[-2]
# OUT: 'i'
name[0:4]
# OUT: 'Zoph'
'Zo' in name
# OUT: True
'z' in name
# OUT: False
'p' not in name
# OUT: False
for i in name:
# OUT:         print('* * * ' + i + ' * * *')

# OUT: * * * Z * * *
# OUT: * * * o * * *
# OUT: * * * p * * *
# OUT: * * * h * * *
# OUT: * * * i * * *
# OUT: * * * e * * *
