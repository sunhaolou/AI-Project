"""
Student Name 1: Haolou Sun
Student Name 2: Longjie Guan

UW NetID: sunhaolo guan123
Student number: 1934592 2272669
CSE 415, Winter 2023, University of Washington
"""
from EightPuzzle import *

goal_state = [[0,1,2],[3,4,5],[6,7,8]]

x_axis_of_goal_state = [0,0,0,1,1,1,2,2,2]
y_axis_of_goal_state = [0,1,2,0,1,2,0,1,2]

def h(s):
    """ This function returns the manhattan distance to the goal state for each puzzle. """
    sum_of_distance = 0                          # Create a valuable represents the sum of Manhattan distance of every puzzles
    for i in range (3):
        for j in range (3):
            if s.b[i][j] == 0:                    # If the puzzle value is 0, ignore this one
                continue
            #elif s[i][j] == goal_state[i][j]:   # If the target puzzle postion is the same as goal state puzzle position, the Manhattan distance i 0
            #    sum_of_distance += 0
            else:
                evl = s.b[i][j]
                if evl == 1:
                    x_dif = abs(0 - i)
                    y_dif = abs(1 - j)
                    Mah_dis = x_dif + y_dif
                    sum_of_distance += Mah_dis
                elif evl == 2:
                    x_dif = abs(0 - i)
                    y_dif = abs(2 - j)
                    Mah_dis = x_dif + y_dif
                    sum_of_distance += Mah_dis
                elif evl == 3:
                    x_dif = abs(1 - i)
                    y_dif = abs(0 - j)
                    Mah_dis = x_dif + y_dif
                    sum_of_distance += Mah_dis
                elif evl == 4:
                    x_dif = abs(1 - i)
                    y_dif = abs(1 - j)
                    Mah_dis = x_dif + y_dif
                    sum_of_distance += Mah_dis
                elif evl == 5:
                    x_dif = abs(1 - i)
                    y_dif = abs(2 - j)
                    Mah_dis = x_dif + y_dif
                    sum_of_distance += Mah_dis
                elif evl == 6:
                    x_dif = abs(2 - i)
                    y_dif = abs(0 - j)
                    Mah_dis = x_dif + y_dif
                    sum_of_distance += Mah_dis
                elif evl == 7:
                    x_dif = abs(2 - i)
                    y_dif = abs(1 - j)
                    Mah_dis = x_dif + y_dif
                    sum_of_distance += Mah_dis
                elif evl == 8:
                    x_dif = abs(2 - i)
                    y_dif = abs(2 - j)
                    Mah_dis = x_dif + y_dif
                    sum_of_distance += Mah_dis
    return sum_of_distance