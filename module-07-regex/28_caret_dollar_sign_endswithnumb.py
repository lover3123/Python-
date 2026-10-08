# Ch7 | 28/46 | The Caret and Dollar Sign Characters [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
# OUT: <_sre.SRE_Match object; span=(16, 17), match='2'>
endsWithNumber.search('Your number is forty two.') == None
# OUT: True
