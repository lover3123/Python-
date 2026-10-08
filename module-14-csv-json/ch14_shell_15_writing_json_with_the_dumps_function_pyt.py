"""Chapter 14: CSV Files and JSON Data
Section: Writing JSON with the dumps() Function
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter14
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch14: csv, json
File: ch14_shell_15_writing_json_with_the_dumps_function_pyt.py (15 of 21 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
# OUT: 'felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)
stringOfJsonData
# OUT: '{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'
