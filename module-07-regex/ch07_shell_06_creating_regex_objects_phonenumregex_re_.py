"""Chapter 7: Pattern Matching with Regular Expressions
Section: Creating Regex Objects
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_06_creating_regex_objects_phonenumregex_re_.py (6 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
