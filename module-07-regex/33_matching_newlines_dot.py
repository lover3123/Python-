# Ch7 | 33/46 | Matching Newlines with the Dot Character [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.
# OUT: \nUphold the law.').group()
# OUT: 'Serve the public trust.'

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.
# OUT: \nUphold the law.').group()
# OUT: 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
