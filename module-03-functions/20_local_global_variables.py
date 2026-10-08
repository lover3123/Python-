# Ch3 | 20/41 | Local and Global Variables with the Same Name [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter3

   def spam():
     eggs = 'spam local'
       print(eggs) # prints 'spam local'
   def bacon():

     eggs = 'bacon local'
       print(eggs) # prints 'bacon local'
       spam()
       print(eggs) # prints 'bacon local'

 eggs = 'global'
   bacon()
   print(eggs) # prints 'global'
