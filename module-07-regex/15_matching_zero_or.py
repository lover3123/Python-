# Ch7 | 15/46 | Matching Zero or More with the Star [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
# OUT: 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
# OUT: 'Batwoman'

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
# OUT: 'Batwowowowoman'
