# Ch7 | 13/46 | Optional Matching with the Question Mark [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
# OUT: 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
# OUT: 'Batwoman'
