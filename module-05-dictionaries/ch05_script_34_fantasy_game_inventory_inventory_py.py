"""Chapter 5: Dictionaries and Structuring Data
Section: Fantasy Game Inventory
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter5
Type: book script/example
PPT map: Syllabus Ch5: dicts, structuring data
File: ch05_script_34_fantasy_game_inventory_inventory_py.py (34 of 37 in this chapter)
"""

# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
