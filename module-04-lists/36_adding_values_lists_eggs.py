# Ch4 | 36/62 | Adding Values to Lists with the append() and insert() Methods [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

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
