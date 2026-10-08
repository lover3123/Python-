# Ch5 | 16/37 | The setdefault() Method [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter5

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
