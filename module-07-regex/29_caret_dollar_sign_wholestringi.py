# Ch7 | 29/46 | The Caret and Dollar Sign Characters [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
# OUT: <_sre.SRE_Match object; span=(0, 10), match='1234567890'>
wholeStringIsNum.search('12345xyz67890') == None
# OUT: True
wholeStringIsNum.search('12 34567890') == None
# OUT: True
