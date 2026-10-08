# Ch3 | 18/41 | Local Scopes Cannot Use Variables in Other Local Scopes [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter3

  def spam():
    eggs = 99
    bacon()
    print(eggs)

  def bacon():
      ham = 101
    eggs = 0

 spam()
