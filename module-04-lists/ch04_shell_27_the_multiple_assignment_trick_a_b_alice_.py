"""Chapter 4: Lists
Section: The Multiple Assignment Trick
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter4
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: PPT Module-3: list create/index/slicing, len/append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy, +/*, in/not in, del
File: ch04_shell_27_the_multiple_assignment_trick_a_b_alice_.py (27 of 62 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

a, b = 'Alice', 'Bob'
a, b = b, a
print(a)
# OUT: 'Bob'
print(b)
# OUT: 'Alice'
