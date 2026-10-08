"""Chapter 4: Lists
Section: Converting Types with the list() and tuple() Functions
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_54_converting_types_with_the_list_and_tuple.py (54 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

tuple(['cat', 'dog', 5])
# OUT: ('cat', 'dog', 5)
list(('cat', 'dog', 5))
# OUT: ['cat', 'dog', 5]
list('hello')
# OUT: ['h', 'e', 'l', 'l', 'o']
