"""Chapter 7: Pattern Matching with Regular Expressions
Section: Managing Complex Regexes
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: book script/example
PPT map: Syllabus Ch7: regex
File: ch07_script_38_managing_complex_regexes_phoneregex_re_c.py (38 of 46 in this chapter)
"""

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?)')
