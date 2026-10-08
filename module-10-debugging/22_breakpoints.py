# Ch10 | 22/24 | Breakpoints [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter10

   import random
   heads = 0
   for i in range(1, 1001):
     if random.randint(0, 1) == 1:
           heads = heads + 1
       if i == 500:
         print('Halfway done!')
   print('Heads came up ' + str(heads) + ' times.')
