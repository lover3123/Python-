"""Chapter 4: Lists
Section: Removing Values from Lists with remove()
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_38_removing_values_from_lists_with_remove_s.py (38 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('chicken')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#11>", line 1, in <module>
# OUT:     spam.remove('chicken')
# OUT: ValueError: list.remove(x): x not in list
