# Ch7 | 35/46 | Case-Insensitive Matching [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

robocop = re.compile(r'robocop', re.I)
robocop.search('Robocop is part man, part machine, all cop.').group()
# OUT: 'Robocop'

robocop.search('ROBOCOP protects the innocent.').group()
# OUT: 'ROBOCOP'

robocop.search('Al, why does your programming book talk about robocop so much?').group()
# OUT: 'robocop'
