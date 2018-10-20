#-------------------------------------------------
# Nathan Saccon (20576843)
# CS 116 Winter 2015
# Assignment 5 Question 2 (Participation Function)
#-------------------------------------------------

import math
import check

# * Participation Function *
# participation(correct, incorrect, unanswered, threshold, tutorials_attended) Produces the
#    participation mark from the 'correct' 'incorrect' and 'unanswered' questions based
#    on the 'threshold' and then adds a bonus based on 'tutorials_attended'.
# participation: Nat Nat Nat Float Nat -> Float
# Requires: correct + incorrect + unanswered > 0
#           0 < threshold <= 100
#           0 < tutorials_attended <= 12
# Examples:
# participation(30,0,0,100,0) => 5.0
# participation(10,15,5,80,0) => 3.541666


def participation(correct, incorrect, unanswered, threshold, tutorials_attended):
    overall_percent = 5
    total_points = (2 * correct) + incorrect
    total_questions = (correct + incorrect + unanswered)
    questions_counted = math.ceil(total_questions * (threshold / 100))
    possible_points = 2 * questions_counted
    if questions_counted <= correct:
        return 5.0
    if questions_counted <= (correct + incorrect):
        return min((((2 * correct + (questions_counted - correct)) / possible_points) \
                    * overall_percent) + tutorials_attended * 0.1, 5.0)
    else:
        return min((((2 * correct + incorrect) / possible_points) * overall_percent) \
                   + tutorials_attended * 0.1 ,5.0)


# Tests for particitation:
check.expect("Q2T1",participation(30,0,0,100,0),5.0)
check.within("Q2T2",participation(10,15,5,80,0), 3.541666,0.0001)
check.within("Q2T3",participation(10,15,5,90,0), 3.240740,0.0001)
check.within("Q2T4",participation(15,5,0,90,0), 4.583333,0.0001)
check.within("Q2T5",participation(20,5,5,90,5), 4.666666,0.0001)
check.expect("Q2T6",participation(42,8,0,95,0),4.6875)
check.expect("Q2T7",participation(42,8,0,95,3),4.9875)
check.expect("Q2T8",participation(42,8,0,95,4),5.0)
check.within("Q2T9",participation(22,3,4,90,0), 4.351851,0.0001)
check.expect("Q2T10",participation(22,3,4,90,12),5.0)
check.expect("Q2T11",participation(0,0,30,21,4),0.4)
