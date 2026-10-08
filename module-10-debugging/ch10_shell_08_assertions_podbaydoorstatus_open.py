"""Chapter 10: Debugging
Section: Assertions
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter10
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch10: raise, assert, logging, debugger
File: ch10_shell_08_assertions_podbaydoorstatus_open.py (8 of 24 in this chapter)
"""

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
