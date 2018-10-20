#-----------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 6 Question 4 (Turn 6nimmt Function)
#-----------------------------------------------

import math
import check

## A Card_6Nimmt is a Nat between 1 and 104, inclusive.
## A Row_6Nimmt is a (listof Card_6Nimmt) containing between 1 and 5 values,
##   in strictly increasing order.
## A Board_6Nimmt is a (listof Row_6Nimmt) of length 4. There are
##   no duplicates between any of the Row_6Nimmt lists in the board.

## Sample board
my_board = [[67, 70], [9, 18, 19], [8], [13, 30, 50, 88, 93]]
## String constant for printing
prompt = "Enter choice: "
## Constant for full row size
full_row = 5

# * Turn 6nimmt Function *
# turn_6nimmt(board, card) Produces True if 'card' can be played on 'board' directly. And produces the row
#     taken if a row needs to be taken off for 'card' to be played on 'board'.
# turn_6nimmt: Board_6Nimmt Card_6Nimmt -> (anyof True Row_6Nimmt)
# Effects:
# - Mutates row if a card can be played
# - Mutates board if a row has to be removed
# Examples:


def turn_6nimmt(board, card):
    last_card1 = board[0][-1]
    last_card2 = board[1][-1]
    last_card3 = board[2][-1]
    last_card4 = board[3][-1]
    if card < last_card1 and card < last_card2 and card < last_card3 and card < last_card4:
        print('Enter 1 for ' + str(board[0])+'\nEnter 2 for ' + str(board[1]) +'\nEnter 3 for ' + str(board[2]) \
                    +'\nEnter 4 for ' + str(board[3]) +'\n')
        row = input(prompt)
        row_num = int(row) - 1
        old_row = board[row_num]
        board[row_num] = [card]
        return old_row
    row_to_enter = min(filter(lambda x:x>0, [card-last_card1,card-last_card2,card-last_card3,card-last_card4]))
    if card-last_card1 == row_to_enter and card > last_card1 and len(board[0]) < 5:
        board[0] = board[0] + [card]
        return True
    if card-last_card2 == row_to_enter and card > last_card2 and len(board[1]) < 5:
            board[1] = board[1] + [card]
            return True
    if card-last_card3 == row_to_enter and card > last_card3 and len(board[2]) < 5:
        board[2] = board[2] + [card]
        return True
    if card-last_card4 == row_to_enter and card > last_card4 and len(board[3]) < 5:
            board[3] = board[3] + [card]
            return True
    if card-last_card1 == row_to_enter and card > last_card1 and len(board[0]) == 5:
        old_row = board[0]
        board[0] = [card]
        return old_row
    if card-last_card2 == row_to_enter and card > last_card2 and len(board[1]) == 5:
            old_row = board[1]
            board[1] = [card]
            return old_row
    if card-last_card3 == row_to_enter and card > last_card3 and len(board[2]) == 5:
        old_row = board[2]
        board[2] = [card]
        return old_row
    if card-last_card4 == row_to_enter and card > last_card4 and len(board[3]) == 5:
            old_row = board[3]
            board[3] = [card]
            return old_row



# Tests for turn_6nimmt
check.expect('Q4T1a',turn_6nimmt(my_board, 71), True)
check.expect('Q4T1b', my_board, [[67, 70, 71], [9, 18, 19], [8], [13, 30, 50, 88, 93]])
check.expect('Q4T2a',turn_6nimmt(my_board, 94), [13, 30, 50, 88, 93])
check.expect('Q4T2b', my_board, [[67, 70, 71], [9, 18, 19], [8], [94]])
check.expect('Q4T3a',turn_6nimmt(my_board, 25), True)
check.expect('Q4T3b', my_board, [[67, 70, 71], [9, 18, 19, 25], [8], [94]])
check.set_input(['2'])
check.set_screen('Choose one of the rows')
check.expect('Q4T4a',turn_6nimmt(my_board, 5), [9, 18, 19, 25])
check.expect('Q4T4b', my_board, [[67, 70, 71], [5], [8], [94]])
check.expect('Q4T5a',turn_6nimmt(my_board, 9), True)
check.expect('Q4T5b', my_board, [[67, 70, 71], [5], [8, 9], [94]])
check.expect('Q4T6a',turn_6nimmt(my_board, 10), True)
check.expect('Q4T6b', my_board, [[67, 70, 71], [5], [8, 9, 10], [94]])
check.expect('Q4T7a',turn_6nimmt(my_board, 11), True)
check.expect('Q4T7b', my_board, [[67, 70, 71], [5], [8, 9, 10, 11], [94]])
check.set_input(['3'])
check.set_screen('Choose one of the rows')
check.expect('Q4T8a',turn_6nimmt(my_board, 2), [8, 9, 10, 11])
check.expect('Q4T8b', my_board, [[67, 70, 71], [5], [2], [94]])
check.expect('Q4T9a',turn_6nimmt(my_board, 72), True)
check.expect('Q4T9b', my_board, [[67, 70, 71, 72], [5], [2], [94]])
check.expect('Q4T10a',turn_6nimmt(my_board, 73), True)
check.expect('Q4T10b', my_board, [[67, 70, 71, 72, 73], [5], [2], [94]])
check.expect('Q4T11a',turn_6nimmt(my_board, 93), [67, 70, 71, 72, 73])
check.expect('Q4T11b', my_board, [[93], [5], [2], [94]])
