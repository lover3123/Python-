# Ch3 | 22/41 | The global Statement [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter3

  def spam():
    global eggs
    eggs = 'spam'

  eggs = 'global'
  spam()
  print(eggs)
