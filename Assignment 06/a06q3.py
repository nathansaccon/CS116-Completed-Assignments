#----------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 6 Question 3 (Search Piazza)
#----------------------------------------------

import math
import check

# (global) Constants for examples and tests
post507 = "@507::empty in Q1/Q2::can list be empty::yes"
post19 = "@19::Allowable functions::empty?, first, rest::"
post1 = "@1::CS116 W2015::Welcome to first post::Thanks!"
cs116 =   [post507, post1, post19]

# * Search Piazza *
# search_piazza(posts, keyword) Produces a lift of the 'posts' numbers that contain the 'keyword'
# search_piazza: (listof Str) Str -> (listof Int)
# Requires: keyword non-empty
# Examples:
# search_piazza([], keyword) => []
# search_piazza([post19,post507], 'All') => [19]


def search_piazza(posts, keyword):
    if posts == []: return []
    else:
        list_with_key = filter(lambda x:keyword in x, posts)
        return list(map(lambda str:int(str[1:str.find(':')]), list_with_key))


# Tests for search_piazza
check.expect('Q3T1',search_piazza([],'can'), [])
check.expect('Q3T2',search_piazza(cs116,':'), [507,1,19])
check.expect('Q3T3',search_piazza(cs116,'All'), [19])
check.expect('Q3T4',search_piazza(cs116,'empty'), [507,19])
check.expect('Q3T5',search_piazza(cs116,'Welcome'), [1])
check.expect('Q3T6',search_piazza(cs116,'Jimmy'), [])
check.expect('Q3T7',search_piazza(cs116,'1'), [507,1,19])
check.expect('Q3T8',search_piazza(cs116,'yes'), [507])
check.expect('Q3T9',search_piazza(cs116,'first'), [1,19])