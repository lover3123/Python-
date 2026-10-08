# Ch7 | 11/46 | Matching Multiple Groups with the Pipe [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()
# OUT: 'Batman'

mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()
# OUT: 'Tina Fey'
