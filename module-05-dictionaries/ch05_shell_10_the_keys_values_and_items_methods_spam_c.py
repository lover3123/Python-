"""Chapter 5: Dictionaries and Structuring Data
Section: The keys(), values(), and items() Methods
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter5
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch5: dicts, structuring data
File: ch05_shell_10_the_keys_values_and_items_methods_spam_c.py (10 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
# OUT:         print('Key: ' + k + ' Value: ' + str(v))

# OUT: Key: age Value: 42
# OUT: Key: color Value: red
