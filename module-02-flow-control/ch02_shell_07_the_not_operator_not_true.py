"""Chapter 2: Flow Control
Section: The not Operator
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter2
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-1: boolean, comparison, if/else/elif, while, break/continue, for/range, import, sys.exit
File: ch02_shell_07_the_not_operator_not_true.py (7 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

not True
# OUT:           False
not not not not True
# OUT:           True
