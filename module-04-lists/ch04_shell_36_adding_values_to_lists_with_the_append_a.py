"""Chapter 4: Lists
Section: Adding Values to Lists with the append() and insert() Methods
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_36_adding_values_to_lists_with_the_append_a.py (36 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

eggs = 'hello'
eggs.append('world')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#19>", line 1, in <module>
# OUT:     eggs.append('world')
# OUT: AttributeError: 'str' object has no attribute 'append'
bacon = 42
bacon.insert(1, 'world')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#22>", line 1, in <module>
# OUT:     bacon.insert(1, 'world')
# OUT: AttributeError: 'int' object has no attribute 'insert'
