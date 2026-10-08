# Ch14 | 14/21 | Reading JSON with the loads() Function [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter14

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,
# OUT: "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue
# OUT: {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
