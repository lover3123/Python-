# Ch14 | 15/21 | Writing JSON with the dumps() Function [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter14

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
# OUT: 'felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)
stringOfJsonData
# OUT: '{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'
