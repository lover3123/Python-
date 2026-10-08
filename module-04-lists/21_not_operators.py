# Ch4 | 21/62 | The in and not in Operators [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'howdy' in ['hello', 'hi', 'howdy', 'heyas']
# OUT: True
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam
# OUT: False
'howdy' not in spam
# OUT: False
'cat' not in spam
# OUT: True
