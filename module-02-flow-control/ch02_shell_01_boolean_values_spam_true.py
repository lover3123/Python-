"""Chapter 2: Flow Control
Section: Boolean Values
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter2
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-1: boolean, comparison, if/else/elif, while, break/continue, for/range, import, sys.exit
File: ch02_shell_01_boolean_values_spam_true.py (1 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

# OUT: ? >>> spam = True
spam
# OUT:            True
# OUT:         ? >>> true
# OUT:            Traceback (most recent call last):
# OUT:              File "<pyshell#2>", line 1, in <module>
# OUT:                true
# OUT:            NameError: name 'true' is not defined
# OUT:         ? >>> True = 2 + 2
# OUT:            SyntaxError: assignment to keyword
