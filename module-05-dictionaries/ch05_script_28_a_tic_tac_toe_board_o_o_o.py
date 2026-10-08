"""Chapter 5: Dictionaries and Structuring Data
Section: A Tic-Tac-Toe Board
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter5
Type: book script/example
PPT map: Syllabus Ch5: dicts, structuring data
File: ch05_script_28_a_tic_tac_toe_board_o_o_o.py (28 of 37 in this chapter)
"""

O|O|O
-+-+-
Traceback (most recent call last):
  File "ticTacToe.py", line 10, in <module>
    printBoard(theBoard)
  File "ticTacToe.py", line 6, in printBoard
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
KeyError: 'mid-L'
