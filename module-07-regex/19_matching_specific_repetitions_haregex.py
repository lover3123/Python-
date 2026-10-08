# Ch7 | 19/46 | Matching Specific Repetitions with Curly Brackets [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
# OUT: 'HaHaHa'

mo2 = haRegex.search('Ha')
mo2 == None
# OUT: True
