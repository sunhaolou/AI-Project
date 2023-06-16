'''Farmer_Fox.py
by Haolou Sun
UWNetID: sunhaolo
Student number: 1934592

Assignment 2, in CSE 415, Winter 2023.

This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

Farmer=0  # array index to access farmer position
Fox=1  # same idea for fox
Chicken=2 # same idea for chicken
Grain=3 # same idea for grain

class State():

  def __init__(self, d=None):
    self.d = d

  def __eq__(self,s2):
    for i in range(4):
      if self.d[i] != s2.d[i]:
        return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    if self.d[Farmer] == 1:
      txt = "\n Farmer on left \n"
    else:
      txt = "\n Farmer on right \n"
    if self.d[Fox] == 1:
      txt += " Fox on left \n"
    else:
      txt += " Fox on right \n"
    if self.d[Chicken] == 1:
      txt += " Chicken on left \n"
    else:
      txt += " Chicken on right \n"
    if self.d[Grain] == 1:
      txt += " Grain on left.\n"
    else:
      txt += " Grain on right.\n"
    return txt

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State()
    news.d=[]
    for i in range(4):
      news.d.append(self.d[i])
    return news

  def can_move(self,F,f,c,g):
    '''Tests whether it's legal to move the farmer, fox
     chicken or grain.'''
    p = self.d
    if F != 1:
      return False # Need the farmer.
    farmer_pos = abs(p[Farmer] - 1)
    fox_pos = abs(p[Fox] - f)
    chicken_pos = abs(p[Chicken] - c)
    grain_pos = abs(p[Grain] - g)
    if farmer_pos == 1:
      if fox_pos == 0 and chicken_pos == 0:
        return False
      if chicken_pos == 0 and grain_pos == 0:
        return False
    else:
      if fox_pos == 1 and chicken_pos == 1:
        return False
      if chicken_pos == 1 and grain_pos == 1:
        return False
    return True


  def move(self,F,f,c,g):
    '''Assuming it's legal to make the move, this computes the new state
      resulting from moving the farmer, fox, chicken and grain.'''
    news = self.copy()
    p = news.d
    p[Farmer] = abs(p[Farmer] - F)
    p[Fox] = abs(p[Fox] - f)
    p[Chicken] = abs(p[Chicken] - c)
    p[Grain] = abs(p[Grain] - g)
    return news

def goal_test(s):
  '''If farmer, fox, chicken and grain are on the right, then s is a goal state.'''
  p = s.d
  return (p == [0,0,0,0])

def goal_message(s):
  return "Congratulations on successfully taking fox, chicken and grain across the creek!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
CREATE_INITIAL_STATE = lambda : State(d=[1,1,1,1])
#</INITIAL_STATE>

#<OPERATORS>
Ffcg_combinations = [(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,1,0,0)]

OPERATORS = [Operator(
  "Cross the creek with "+str(F)+" farmer, "+str(f)+" fox, "+str(c)+" chicken, "
  +str(g)+" and grain. ",
  lambda s, F1=F, f1=f, c1=c, g1=g: s.can_move(F1,f1,c1,g1),
  lambda s, F1=F, f1=f, c1=c, g1=g: s.move(F1,f1,c1,g1))
  for (F,f,c,g) in Ffcg_combinations]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>