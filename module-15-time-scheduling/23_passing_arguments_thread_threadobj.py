# Ch15 | 23/37 | Passing Arguments to the Thread’s Target Function [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
