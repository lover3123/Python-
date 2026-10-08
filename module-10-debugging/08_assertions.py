# Ch10 | 08/24 | Assertions [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter10

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#10>", line 1, in <module>
# OUT:     assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# OUT: AssertionError: The pod bay doors need to be "open".
