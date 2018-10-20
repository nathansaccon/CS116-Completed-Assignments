#----------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 7 Question 3 (Alternating)
#----------------------------------------------

import math
import check

# * Find W * (HELPER)
# find_w(s,pos) Produces True if there is a w value in 's' that starts after or at 'pos'
#     and can create the string 's' by repetitively alternating, and False otherwise.
# find_w: Str Nat -> Bool


def find_w(s,pos):
    w = s[:pos]
    lw = len(w)
    ex = s[:len(s) - lw]
    if pos == math.ceil(len(s)/2):
        return False
    if ex == ex[::-1]:
        return True
    else:
        return find_w(s,pos+1)

#----------------------------------------------------------------------------------------


# * Alternating Function *
# alternating(s) Produces true if string 's' is repetitively alternating and false otherwise.
# alternating: str -> Bool
# Examples:
# alternating('') => True
# alternating('a') => True


def alternating(s):
    if len(s) <= 1:
        return True
    if s == s[::-1] and len(s)%2 == 0:
        return True
    else:
        return find_w(s,2)


# Tests for alternating
check.expect('Q3T1',alternating(''),True)
check.expect('Q3T2',alternating('a'),True)
check.expect('Q3T3',alternating('bobbob'),True)
check.expect('Q3T4',alternating('bobbobbob'),True)
check.expect('Q3T5',alternating('abbaabba'),True)
check.expect('Q3T6',alternating('TT'),True)
check.expect('Q3T7',alternating('ababba'),False)
check.expect('Q3T8',alternating('ababbaba'),True)
check.expect('Q3T9',alternating('z1881zz1881z'),True)
check.expect('Q3T10',alternating('z1881zz1881zz18'),True)
check.expect('Q3T11',alternating('Hello There'),False)
check.expect('Q3T12',alternating('TTT12345678'),False)
check.expect('Q3T13',alternating('bobkbob'),False)

