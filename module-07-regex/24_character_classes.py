# Ch7 | 24/46 | Character Classes [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7
# OUT: swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# OUT: ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6
# OUT: geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
