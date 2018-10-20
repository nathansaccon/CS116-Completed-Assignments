#--------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 5 Question 1 (Next In Sequence)
#--------------------------------------------

import math
import check

# * Next In Sequence Function *
# next_in_sequence(a,b,c) Produces the next number in the arithmetic sequence
#   if 'a' 'b' and 'c' are the start of a squence, and false otherwise.
# next_in_sequence: (anyof Int Float) -> (anyof Int False)
# Examples:
# next_in_sequence(1,2,3) => 4
# next_in_sequence(2,4,7) => False


def next_in_sequence(a,b,c):
    diff = a - b
    if (a - b) == (b - c):
        return c - diff
    else:
        return False

# Tests for next_in_sequence:
check.expect("Q1T1",next_in_sequence(1,2,3),4)
check.expect("Q1T2",next_in_sequence(2,4,7),False)
check.expect("Q1T3",next_in_sequence(2,4,6),8)
check.expect("Q1T4",next_in_sequence(-1,0,1),2)
check.expect("Q1T5",next_in_sequence(-5,-3,-1),1)
check.expect("Q1T6",next_in_sequence(-250,-200,-150),-100)
check.expect("Q1T7",next_in_sequence(2,4,0),False)
check.expect("Q1T8",next_in_sequence(-20,-15,10),False)
check.expect("Q1T9",next_in_sequence(2.5,5,7.5),10)
