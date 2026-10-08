# Ch4 | 48/62 | Mutable and Immutable Data Types [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter4

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
name
# OUT: 'Zophie a cat'
newName
# OUT: 'Zophie the cat'
