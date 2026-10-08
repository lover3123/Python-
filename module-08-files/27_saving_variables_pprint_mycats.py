# Ch8 | 27/40 | Saving Variables with the pprint.pformat() Function [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import myCats
myCats.cats
# OUT: [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
myCats.cats[0]
# OUT: {'name': 'Zophie', 'desc': 'chubby'}
myCats.cats[0]['name']
# OUT: 'Zophie'
