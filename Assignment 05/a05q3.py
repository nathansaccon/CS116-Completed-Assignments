#----------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 5 Question 3 (Fibonacci Functions)
#----------------------------------------------

import math
import check

# * Fibonacci Maker * (Helper)
# fib_maker(prev,prev2,num,n) Produces the 'n'th fibonacci number where 'num'
#    'prev' and 'prev2' represent the starting point on the fibonacci number line
# fib_maker: Nat Nat Nat Nat -> Nat
def fib_maker(prev,prev2,num,n):
    next_num = prev + prev2
    if num == n:
        return prev
    else:
        return fib_maker(prev2,next_num,(num + 1),n)


# * Fibonacci Function Part A *
# fib_rec(n) Produces the 'n'th fibonacci number
# fib_rec: Nat -> Nat
# Examples
# fib_rec(1) => 1
# fib_rec(6) => 8


def fib_rec(n):
    nth_num = fib_maker(0,1,0,n)
    return nth_num


# Tests for fib_rec
check.expect("Q3aT0",fib_rec(0),0)
check.expect("Q3aT1",fib_rec(1),1)
check.expect("Q3aT2",fib_rec(6),8)
check.expect("Q3aT3",fib_rec(11),89)
check.expect("Q3aT4",fib_rec(8),21)
check.expect("Q3aT5",fib_rec(13),233)
check.expect("Q3aT6",fib_rec(15),610)
check.expect("Q3aT7",fib_rec(17),1597)
check.expect("Q3aT8",fib_rec(43),433494437)

#----------------------------------------------------------------------------

# * Fibonacci Function B *
# fib_approx(n) Produces the 'n'th fibonacci number
# fib_approx: Nat -> Nat
# Requires: n <= 71
# Examples:
# fib_approx(1) => 1
# fib_approx(6) => 8

def fib_approx(n):
    phi = (1 + math.sqrt(5)) / 2
    Fn = (phi**n - (-phi)**-n) / math.sqrt(5)
    Fn = int(Fn)
    return Fn


# Tests for fib_approx
check.expect("Q3bT0",fib_approx(0),0)
check.expect("Q3bT1",fib_approx(1),1)
check.expect("Q3bT2",fib_approx(6),8)
check.expect("Q3bT3",fib_approx(8),21)
check.expect("Q3bT4",fib_approx(15),610)
check.expect("Q3bT5",fib_approx(43),433494437)
check.expect("Q3bT6",fib_approx(55),139583862445)
check.expect("Q3bT7",fib_approx(71),308061521170129)

