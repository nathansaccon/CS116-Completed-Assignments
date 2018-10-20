#---------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 5 Question 4 (Multiple Of Seven)
#---------------------------------------------

import math
import check

# * Multiple of Seven Function *
# mult_of_7(n) Checks if 'n' is a multiple of 7.
# mult_of_7: Nat -> Bool
# Examples:
# mult_of_7(0) => True
# mult_of_7(15) => False


def mult_of_7(n):
    if n == 0 or n == 7:
        return True
    if n <= 10:
        return False
    else:
        dub_last_digit = (n % 10) * 2
        rest_digits = n // 10
        n_hat = abs(rest_digits - dub_last_digit)
        return mult_of_7(n_hat)


# Tests for mult_of_7:
check.expect("Q4T1",mult_of_7(0),True)
check.expect("Q4T2",mult_of_7(15),False)
check.expect("Q4T3",mult_of_7(7),True)
check.expect("Q4T4",mult_of_7(49),True)
check.expect("Q4T5",mult_of_7(21),True)
check.expect("Q4T6",mult_of_7(28),True)
check.expect("Q4T7",mult_of_7(63),True)
check.expect("Q4T8",mult_of_7(44),False)
check.expect("Q4T9",mult_of_7(54),False)
check.expect("Q4T10",mult_of_7(99),False)
check.expect("Q4T11",mult_of_7(336),True)
check.expect("Q4T12",mult_of_7(4305),True)
check.expect("Q4T13",mult_of_7(2146),False)
check.expect("Q4T14",mult_of_7(1331),False)