"""Chapter 14: CSV Files and JSON Data
Section: Step 2: Download the JSON Data
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter14
Type: book script/example
PPT map: Syllabus Ch14: csv, json
File: ch14_script_17_step_2_download_the_json_data_python3.py (17 of 21 in this chapter)
"""

#! python3
# quickWeather.py - Prints the weather for a location from the command line.

--snip--

# Download the JSON data from OpenWeatherMap.org's API.
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# TODO: Load JSON data into a Python variable.
