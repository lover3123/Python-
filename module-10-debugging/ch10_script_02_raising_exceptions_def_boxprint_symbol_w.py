"""Chapter 10: Debugging
Section: Raising Exceptions
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter10
Type: book script/example
PPT map: Syllabus Ch10: raise, assert, logging, debugger
File: ch10_script_02_raising_exceptions_def_boxprint_symbol_w.py (2 of 24 in this chapter)
"""

   def boxPrint(symbol, width, height):
       if len(symbol) != 1:
         raise Exception('Symbol must be a single character string.')
       if width <= 2:
         raise Exception('Width must be greater than 2.')
       if height <= 2:
         raise Exception('Height must be greater than 2.')
       print(symbol * width)
       for i in range(height - 2):
           print(symbol + (' ' * (width - 2)) + symbol)
       print(symbol * width)

   for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
       try:
           boxPrint(sym, w, h)
     except Exception as err:
         print('An exception happened: ' + str(err))
