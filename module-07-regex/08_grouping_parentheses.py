# Ch7 | 08/46 | Grouping with Parentheses [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
# OUT: '415'
mo.group(2)
# OUT: '555-4242'
mo.group(0)
# OUT: '415-555-4242'
mo.group()
# OUT: '415-555-4242'
