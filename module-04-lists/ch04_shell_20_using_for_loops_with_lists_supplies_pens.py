"""Chapter 4: Lists
Section: Using for Loops with Lists
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_20_using_for_loops_with_lists_supplies_pens.py (20 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
# OUT:     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# OUT: Index 0 in supplies is: pens
# OUT: Index 1 in supplies is: staplers
# OUT: Index 2 in supplies is: flame-throwers
# OUT: Index 3 in supplies is: binders
