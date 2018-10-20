#----------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 6 Question 2 (6 Nimmt Function)
#----------------------------------------------

import math
import check

# * Card Points * (HELPER)
# card_points(card) Produces the number of points that 'card' is worth
# card_points: Int -> Int
# Requires: 0 < card < 105
def card_points(card):
    if card == 55:
        return 7
    if card % 11 == 0:
        return 5
    if card % 10 == 0:
        return 3
    if card % 5 == 0:
        return 2
    else:
        return 1


# * Points Nimmt Function *
# points_6nimmt(cards) Produces the total number of points earned by 'cards'
# points_6nimmt: (listof Int) -> Int
# Requires: 0 < entry in list < 105, no repeats
# Examples:
# points_6nimmt([]) => 0
# points_6nimmt([1,2,3,4,5]) => 6


def points_6nimmt(cards):
    if cards == []: return 0
    else:
        return sum(map(card_points,cards))


# Tests for points_6nimmt
check.expect('Q2T1',points_6nimmt([]),0)
check.expect('Q2T2',points_6nimmt([1,2,3,4,5]),6)
check.expect('Q2T3',points_6nimmt([55]), 7)
check.expect('Q2T4',points_6nimmt([66]), 5)
check.expect('Q2T5',points_6nimmt([70]), 3)
check.expect('Q2T6',points_6nimmt([35]), 2)
check.expect('Q2T7',points_6nimmt([101]), 1)
check.expect('Q2T8',points_6nimmt([55,66,70,35,101]), 18)
check.expect('Q2T9',points_6nimmt([4,2,100,55,44,21]), 18)
check.expect('Q2T10',points_6nimmt([110,55,3,8,4,83,90,95]), 21)