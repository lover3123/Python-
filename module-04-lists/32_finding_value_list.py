# Ch4 | 32/62 | Finding a Value in a List with the index() Method [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')
# OUT: 0
spam.index('heyas')
# OUT: 3
spam.index('howdy howdy howdy')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#31>", line 1, in <module>
# OUT:     spam.index('howdy howdy howdy')
# OUT: ValueError: 'howdy howdy howdy' is not in list
