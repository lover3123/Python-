# Ch7 | 09/46 | Grouping with Parentheses [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

mo.groups()
# OUT: ('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode)
# OUT: 415
print(mainNumber)
# OUT: 555-4242
