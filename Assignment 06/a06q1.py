#----------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 6 Question 1 (Password Function)
#----------------------------------------------

import math
import check

# * Password Strength Function *
# password_strength (password) Produces False if password does not meet the requirements,
#     and prints says the password failed the basic tests. Otherwise produces the score that
#     reflects the strength of password.
# password_strength: Str -> (anyof False Int)
# Effects:
#  - Prints 'The password X failed a basic test' if the password is invalid
# Examples:
# password_strength('') => False
# password_strength('Aaaa') => -10

def password_strength (password):
    if str.lower(password) == 'password' or password == '' or str.isdigit(password) == True:
        print('The password ' + password + ' failed a basic test')
        return False
    if str.isalpha(password) == True and str.upper(password) == password:
        print('The password ' + password + ' failed a basic test')
        return False
    if str.isalpha(password) == True and str.lower(password) == password:
        print('The password ' + password + ' failed a basic test')
        return False
    starting_score = 0
    uppers = len(list(filter(str.isupper,password)))
    lowers = len(list(filter(str.islower,password)))
    digits = len(list(filter(str.isdigit,password)))
    u_l_and_d = uppers > 0 and lowers > 0 and digits > 0
    special_chars = len(password) - uppers - lowers - digits
    if len(password) < 5:
        score = starting_score - 10
        if u_l_and_d and special_chars == 1:
            return score + 30
        if not(u_l_and_d) and special_chars == 1:
            return  score + 20
        if u_l_and_d and special_chars == 0:
            return score + 10
        if not(u_l_and_d) and special_chars == 0:
            return score
    if len(password) > 8:
        score = starting_score + 10
        if u_l_and_d and special_chars == 1:
            return score + 30
        if not(u_l_and_d) and special_chars == 1:
            return  score + 20
        if u_l_and_d and special_chars == 0:
            return score + 10
        if not(u_l_and_d) and special_chars == 0:
            return score
        if u_l_and_d and special_chars > 1:
            return score + 10 + 20 + (special_chars - 1) * 5
        if not(u_l_and_d) and special_chars > 1:
            return score + 20 + (special_chars - 1) * 5
    else:
        score = starting_score
        if u_l_and_d and special_chars == 1:
            return score + 30
        if not(u_l_and_d) and special_chars == 1:
            return  score + 20
        if u_l_and_d and special_chars == 0:
            return score + 10
        if not(u_l_and_d) and special_chars == 0:
            return score
        if u_l_and_d and special_chars > 1:
            return score + 10 + 20 + (special_chars - 1) * 5
        if not(u_l_and_d) and special_chars > 1:
            return score + 20 + (special_chars - 1) * 5


# Tests for password strength
check.set_screen('The password  failed a basic test')
check.expect('Q1T0',password_strength(''),False)

check.set_screen('The password PassWORd failed a basic test')
check.expect('Q1T1',password_strength('PassWORd'),False)

check.set_screen('The password lowercase failed a basic test')
check.expect('Q1T2',password_strength('lowercase'),False)

check.set_screen('The password UPPERCASE failed a basic test')
check.expect('Q1T3',password_strength('UPPERCASE'), False)

check.set_screen('The password 123456 failed a basic test')
check.expect('Q1T4',password_strength('123456'), False)

check.expect('Q1T5',password_strength('123f'), -10)
check.expect('Q1T6',password_strength('Xy 37 1-0'), 50)
check.expect('Q1T7',password_strength('3L u'), 20)
check.expect('Q1T8',password_strength('3l u'), 10)
check.expect('Q1T9',password_strength('3lLu'), 0)
check.expect('Q1T10',password_strength('LLLL  78a'), 45)
check.expect('Q1T11',password_strength('LLLL  78A'), 35)
check.expect('Q1T12',password_strength('LLLLLL78a'), 20)
check.expect('Q1T13',password_strength('LLLLL 78a'), 40)
check.expect('Q1T14',password_strength('LLLLL 78A'), 30)
check.expect('Q1T15',password_strength('Ul7 LL'), 30)
check.expect('Q1T16',password_strength('UL7 LL'), 20)
check.expect('Q1T17',password_strength('Ul7LLL'), 10)
check.expect('Q1T18',password_strength('UL7LLL'), 0)
check.expect('Q1T19',password_strength('Ul7  LL'), 35)
check.expect('Q1T20',password_strength('UL7  LL'), 25)
check.expect('Q1T21',password_strength('S           u5'), 90)


