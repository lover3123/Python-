# Ch5 | 13/37 | The get() Method [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter5

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#34>", line 1, in <module>
# OUT:     'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
# OUT: KeyError: 'eggs'
