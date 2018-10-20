#--------------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 7 Question 4 (ith In Sorted Function)
#--------------------------------------------------

import math
import check

# * ith In Sorted Function *
# ith_in_sorted(lst, i) Produces the integer at position 'i' if 'lst' was sorted to be accending.
# ith_in_sorted: (listof Int) Nat -> Int
# Requires: list must contain distinct integers and be non-empty
#           0 <= i < len(lst)
# Examples:
# ith_in_sorted([2],0) => 2
# ith_in_sorted([4,5,3,6,2,0,1], 3) => 3


def ith_in_sorted(lst, i):
    seperator = lst[0]
    smaller = list(filter(lambda x:x < seperator,lst))
    larger = list(filter(lambda x:x > seperator,lst))
    if len(smaller) == i:
        return seperator
    if len(smaller) > i:
        return ith_in_sorted(smaller, i)
    if len(smaller) < i:
        return ith_in_sorted(larger, (i - len(smaller) - 1))


# Tests for ith_in_sorted
check.expect('Q4T1',ith_in_sorted([2], 0),2)
check.expect('Q4T2',ith_in_sorted([4,5,3,6,2,0,1],3), 3)
check.expect('Q4T3',ith_in_sorted([17,-5,3,0,2,100], 2),2)
check.expect('Q4T4',ith_in_sorted([18,0,-23,51,666,-40,400], 0),-40)
check.expect('Q4T5',ith_in_sorted([18,0,-23,51,666,-40,400], 1),-23)
check.expect('Q4T6',ith_in_sorted([18,0,-23,51,666,-40,400], 2),0)
check.expect('Q4T7',ith_in_sorted([18,0,-23,51,666,-40,400], 3),18)
check.expect('Q4T8',ith_in_sorted([18,0,-23,51,666,-40,400], 4),51)
check.expect('Q4T9',ith_in_sorted([18,0,-23,51,666,-40,400], 5),400)
check.expect('Q4T10',ith_in_sorted([18,0,-23,51,666,-40,400], 6),666)
