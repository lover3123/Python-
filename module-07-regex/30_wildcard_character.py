# Ch7 | 30/46 | The Wildcard Character [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# OUT: ['cat', 'hat', 'sat', 'lat', 'mat']
