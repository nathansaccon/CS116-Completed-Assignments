#----------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 7 Question 1 (Singles Function)
#----------------------------------------------

import math
import check

# * Singles Function *
# singles(lst) Produces 'lst' with all duplicates removed and in increasing order.
# singles: (listof Int) -> (listof Int)
# Examples:
# singles([]) => []
# singles([1,2,1,3,4,2]) => [1,2,3,4]


def singles(lst):
    inc_lst = sorted(lst)
    if lst == []:
        return []
    if inc_lst[0] not in inc_lst[1:]:
        return [inc_lst[0]] + singles(inc_lst[1:])
    if inc_lst[0] in inc_lst[1:]:
        return singles(inc_lst[1:])


# Tests for singles
check.expect('Q1T1',singles([]),[])
check.expect('Q1T2',singles([1]),[1])
check.expect('Q1T3',singles([1,2]),[1,2])
check.expect('Q1T4',singles([1,1,2]),[1,2])
check.expect('Q1T5',singles([2,1,1]),[1,2])
check.expect('Q1T6',singles([4,-7,2,4,8,-7,-1]),[-7,-1,2,4,8])
check.expect('Q1T7',singles([1,1,1,1,1,1,1,1,1,1]),[1])
check.expect('Q1T8',singles([6,7,0,3]),[0,3,6,7])
check.expect('Q1T9',singles([-5,-1,0,1,5]),[-5,-1,0,1,5])
check.expect('Q1T10',singles([7,4,5,2,6,3,3,5,3,3,3,3,1,1,8,9]),[1,2,3,4,5,6,7,8,9])

