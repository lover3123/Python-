"""Chapter 14: CSV Files and JSON Data
Section: Step 3: Load JSON Data and Print Weather
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter14
Type: book script/example
PPT map: Syllabus Ch14: csv, json
File: ch14_script_19_step_3_load_json_data_and_print_weather_.py (19 of 21 in this chapter)
"""

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
