# Ch1 | 10/30 | String Concatenation and Replication [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter1

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'Alice' * 'Bob'
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#32>", line 1, in <module>
# OUT:     'Alice' * 'Bob'
# OUT: TypeError: can't multiply sequence by non-int of type 'str'
'Alice' * 5.0
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#33>", line 1, in <module>
# OUT:     'Alice' * 5.0
# OUT: TypeError: can't multiply sequence by non-int of type 'float'
