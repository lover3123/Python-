# Ch7 | 03/46 | Finding Patterns of Text Without Regular Expressions [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

   message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
   for i in range(len(message)):
     chunk = message[i:i+12]
     if isPhoneNumber(chunk):
         print('Phone number found: ' + chunk)
   print('Done')
