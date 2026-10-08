"""Chapter 4: Lists
Section: Finding a Value in a List with the index() Method
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_32_finding_a_value_in_a_list_with_the_index.py (32 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')
# OUT: 0
spam.index('heyas')
# OUT: 3
spam.index('howdy howdy howdy')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#31>", line 1, in <module>
# OUT:     spam.index('howdy howdy howdy')
# OUT: ValueError: 'howdy howdy howdy' is not in list
