# Ch7 | 27/46 | The Caret and Dollar Sign Characters [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello world!')
# OUT: <_sre.SRE_Match object; span=(0, 5), match='Hello'>
beginsWithHello.search('He said hello.') == None
# OUT: True
