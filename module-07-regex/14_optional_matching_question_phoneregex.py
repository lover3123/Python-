# Ch7 | 14/46 | Optional Matching with the Question Mark [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
# OUT: '415-555-4242'

mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()
# OUT: '555-4242'
