# Ch7 | 16/46 | Matching One or More with the Plus [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
# OUT: 'Batwoman'

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
# OUT: 'Batwowowowoman'

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
# OUT: True
