"""Chapter 14: CSV Files and JSON Data
Section: Reading JSON with the loads() Function
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter14
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch14: csv, json
File: ch14_shell_14_reading_json_with_the_loads_function_str.py (14 of 21 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,
# OUT: "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue
# OUT: {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
