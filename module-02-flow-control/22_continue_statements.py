# Ch2 | 22/37 | continue Statements [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter2

  while True:
      print('Who are you?')
      name = input()
    if name != 'Joe':
        continue
      print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
      if password == 'swordfish':
        break
 print('Access granted.')
