"""Chapter 7: Pattern Matching with Regular Expressions
Section: Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_41_combining_re_ignorecase_re_dotall_and_re.py (41 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
