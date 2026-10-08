"""Chapter 2: Flow Control
Section: Comparison Operators
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter2
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-1: boolean, comparison, if/else/elif, while, break/continue, for/range, import, sys.exit
File: ch02_shell_03_comparison_operators_hello_hello.py (3 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'hello' == 'hello'
# OUT:            True
'hello' == 'Hello'
# OUT:            False
'dog' != 'cat'
# OUT:            True
True == True
# OUT:            True
True != False
# OUT:            True
42 == 42.0
# OUT:            True
42 == '42'
# OUT:            False
