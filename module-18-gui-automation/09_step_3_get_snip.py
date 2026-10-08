# Ch18 | 09/36 | Step 3: Get and Print the Mouse Coordinates [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter18

   #! python3
   # mouseNow.py - Displays the mouse cursor's current position.
   --snip--
           print(positionStr, end='')
         print('\b' * len(positionStr), end='', flush=True)
