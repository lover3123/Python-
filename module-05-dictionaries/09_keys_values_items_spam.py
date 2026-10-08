# Ch5 | 09/37 | The keys(), values(), and items() Methods [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter5

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = {'color': 'red', 'age': 42}
spam.keys()
# OUT: dict_keys(['color', 'age'])
list(spam.keys())
# OUT: ['color', 'age']
