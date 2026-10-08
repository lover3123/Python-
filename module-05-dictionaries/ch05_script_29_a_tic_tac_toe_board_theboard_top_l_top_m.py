"""Chapter 5: Dictionaries and Structuring Data
Section: A Tic-Tac-Toe Board
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter5
Type: book script/example
PPT map: Syllabus Ch5: dicts, structuring data
File: ch05_script_29_a_tic_tac_toe_board_theboard_top_l_top_m.py (29 of 37 in this chapter)
"""

   theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': '
   ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

   def printBoard(board):
       print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
       print('-+-+-')
       print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
       print('-+-+-')
       print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
   turn = 'X'
   for i in range(9):
      printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
      move = input()
      theBoard[move] = turn
      if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
   printBoard(theBoard)
