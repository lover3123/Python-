"""Chapter 4: Lists
Section: List-like Types: Strings and Tuples
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_46_list_like_types_strings_and_tuples_name_.py (46 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

name = 'Zophie'
name[0]
# OUT: 'Z'
name[-2]
# OUT: 'i'
name[0:4]
# OUT: 'Zoph'
'Zo' in name
# OUT: True
'z' in name
# OUT: False
'p' not in name
# OUT: False
for i in name:
# OUT:         print('* * * ' + i + ' * * *')

# OUT: * * * Z * * *
# OUT: * * * o * * *
# OUT: * * * p * * *
# OUT: * * * h * * *
# OUT: * * * i * * *
# OUT: * * * e * * *
