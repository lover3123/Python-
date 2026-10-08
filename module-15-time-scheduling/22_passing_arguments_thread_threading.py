# Ch15 | 22/37 | Passing Arguments to the Thread’s Target Function [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import threading
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],
# OUT: kwargs={'sep': ' & '})
threadObj.start()
# OUT: Cats & Dogs & Frogs
