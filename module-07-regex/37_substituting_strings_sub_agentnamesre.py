# Ch7 | 37/46 | Substituting Strings with the sub() Method [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent
# OUT: Eve knew Agent Bob was a double agent.')
# OUT: A**** told C**** that E**** knew B**** was a double agent.'
