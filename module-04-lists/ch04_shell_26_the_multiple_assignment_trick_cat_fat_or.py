"""Chapter 4: Lists
Section: The Multiple Assignment Trick
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_26_the_multiple_assignment_trick_cat_fat_or.py (26 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

cat = ['fat', 'orange', 'loud']
size, color, disposition, name = cat
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#84>", line 1, in <module>
# OUT:     size, color, disposition, name = cat
# OUT: ValueError: need more than 3 values to unpack
