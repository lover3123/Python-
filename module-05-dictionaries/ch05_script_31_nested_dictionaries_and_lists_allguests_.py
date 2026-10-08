"""Chapter 5: Dictionaries and Structuring Data
Section: Nested Dictionaries and Lists
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter5
Type: book script/example
PPT map: Syllabus Ch5: dicts, structuring data
File: ch05_script_31_nested_dictionaries_and_lists_allguests_.py (31 of 37 in this chapter)
"""

   allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

   def totalBrought(guests, item):
       numBrought = 0
     for k, v in guests.items():
         numBrought = numBrought + v.get(item, 0)
       return numBrought

   print('Number of things being brought:')
   print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
   print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
   print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
   print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
   print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
