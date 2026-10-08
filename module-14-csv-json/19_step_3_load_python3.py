# Ch14 | 19/21 | Step 3: Load JSON Data and Print Weather [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter14

   ! python3
   # quickWeather.py - Prints the weather for a location from the command line.

   --snip--

   # Load JSON data into a Python variable.
   weatherData = json.loads(response.text)
   # Print weather descriptions.
 w = weatherData['list']
   print('Current weather in %s:' % (location))
   print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
   print()
   print('Tomorrow:')
   print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
   print()
   print('Day after tomorrow:')
   print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
