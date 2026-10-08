"""Chapter 4: Lists
Section: The Tuple Data Type
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_51_the_tuple_data_type_eggs_hello_42_0_5.py (51 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

eggs = ('hello', 42, 0.5)
eggs[0]
# OUT: 'hello'
eggs[1:3]
# OUT: (42, 0.5)
len(eggs)
# OUT: 3
