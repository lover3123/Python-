# Ch3 | 24/41 | The global Statement [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter3

  def spam():
  global eggs
    eggs = 'spam' # this is the global

  def bacon():
  eggs = 'bacon' # this is a local
  def ham():
  print(eggs) # this is the global

  eggs = 42 # this is the global
  spam()
  print(eggs)
