"""Chapter 10: Debugging
Section: Raising Exceptions
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter10
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch10: raise, assert, logging, debugger
File: ch10_shell_01_raising_exceptions_raise_exception_this_.py (1 of 24 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

raise Exception('This is the error message.')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#191>", line 1, in <module>
# OUT:     raise Exception('This is the error message.')
# OUT: Exception: This is the error message.
