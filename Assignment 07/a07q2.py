#----------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 7 Question 2 (Smallest Difference)
#----------------------------------------------

import math
import check

# * Smallest Difference Function *
# smallest_diff(numbers) Produces the smallest difference between and two numbers in 'number'.
# smallest_diff: (listof Int) -> Int
# Requires numbers are in non decreasing order
# Examples:
# smallest_diff([]) => 0
# smallest_diff([5,10,25,300]) => 5


def smallest_diff(numbers):
    mid = len(numbers) // 2
    L1 = numbers[:mid+1]
    L2 = numbers[mid:]
    if len(numbers) == 0 or len(numbers) == 1:
        return 0
    if len(numbers) == 2:
        return abs(numbers[0] - numbers[1])
    else:
        return min(smallest_diff(L1),smallest_diff(L2))


# Tests for smallest_diff
check.expect('Q2T1',smallest_diff([]),0)
check.expect('Q2T2',smallest_diff([5,10,25,300]),5)
check.expect('Q2T3',smallest_diff([5,5,5]),0)
check.expect('Q2T4',smallest_diff([6]),0)
check.expect('Q2T5',smallest_diff([5,10,15,20,25,30]),5)
check.expect('Q2T6',smallest_diff([2,4,8,16,32,64]),2)
check.expect('Q2T7',smallest_diff([-10,-5,5,15,60]),5)
check.expect('Q2T8',smallest_diff([-100,-60,-55,-54]),1)
check.expect('Q2T9',smallest_diff([-5,0,2,5,10]),2)
check.expect('Q2T10',smallest_diff([5,500,505,600,650,10000]),5)