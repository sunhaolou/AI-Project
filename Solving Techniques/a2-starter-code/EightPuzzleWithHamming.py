"""
Student Name 1: Haolou Sun
Student Name 2: Longjie Guan

UW NetID: sunhaolo guan123
Student number: 1934592 2272669
CSE 415, Winter 2023, University of Washington
"""
from EightPuzzle import *

goal_state = [[0,1,2],[3,4,5],[6,7,8]]


def h(s):
    """ This function returns the number of hamming for stage S. """
    ct = 0
    for i in range (3):
        for j in range (3):
            if s.b[i][j] == 0:                        # Error with 'State' object is not subscriptable
                continue
            elif s.b[i][j] != goal_state[i][j]:
                ct = ct + 1
    return ct