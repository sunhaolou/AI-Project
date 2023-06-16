









def runUCS():
  '''This is an encapsulation of some setup before running
  UCS, plus running it and then printing some stats.'''
  initial_state = Problem.CREATE_INITIAL_STATE()
  print("Initial State:")
  print(initial_state)
  global COUNT, BACKLINKS, MAX_OPEN_LENGTH, SOLUTION_PATH
  COUNT = 0
  BACKLINKS = {}
  MAX_OPEN_LENGTH = 0
  SOLUTION_PATH = UCS(initial_state)
  print(str(COUNT)+" states expanded.")
  print('MAX_OPEN_LENGTH = '+str(MAX_OPEN_LENGTH))




def UCS(initial_state):
  '''Uniform Cost Search. This is the actual algorithm.'''
  global g, COUNT, BACKLINKS, MAX_OPEN_LENGTH, CLOSED, TOTAL_COST
  CLOSED = {}
  BACKLINKS[initial_state] = None
  #TOTAL_COST = 0

  # The "Step" comments below help relate UCS's implementation to
  # those of Depth-First Search and Breadth-First Search.

# STEP 1a. Put the start state on a priority queue called OPEN
  OPEN = My_Priority_Queue()
  OPEN.insert(initial_state, Problem.h(initial_state))
# STEP 1b. Assign g=0 to the start state.
  g[initial_state]=0.0

# STEP 2. If OPEN is empty, output “DONE” and stop.
  while (len(OPEN) != 0): # ***STUDENTS CHANGE THIS CONDITION***
    # LEAVE THE FOLLOWING CODE IN PLACE TO INSTRUMENT AND/OR DEBUG YOUR IMPLEMENTATION
    if VERBOSE: report(OPEN, CLOSED, COUNT)
    if len(OPEN)>MAX_OPEN_LENGTH: MAX_OPEN_LENGTH = len(OPEN)

# STEP 3. Select the state on OPEN having lowest priority value and call it S.
#         Delete S from OPEN.
#         Put S on CLOSED.
#         If S is a goal state, output its description
    (S,P) = OPEN.delete_min()
    #print("In Step 3, returned from OPEN.delete_min with results (S,P)= ", (str(S), P))
    #CLOSED.append(S)
    CLOSED[S]=P
    #print(OPEN)
    #print(CLOSED)

    if Problem.GOAL_TEST(S):
      # ***STUDENTS CHANGE THE BODY OF THIS IF.***
      #HANDLE THE BACKTRACING, RECORDING THE SOLUTION AND TOTAL COST,
      # AND RETURN THE SOLUTION PATH, TOO.
      TOTAL_COST = P
      return(backtrace(S))
    COUNT += 1

# STEP 4. Generate each successor of S
#         and if it is already on CLOSED, delete the new instance.
    gs=g[S]
    #print(gs)
    for op in Problem.OPERATORS:
      if op.precond(S):
        new_state = op.state_transf(S)
        edge_cost = S.edge_distance(new_state)
        new_g = gs + edge_cost
        new_f = new_g + Problem.h(new_state)

        if (new_state in CLOSED):
          p = CLOSED[new_state]
          if new_f< p:
            OPEN.insert(new_state,new_f)
          else:
              del new_state
              continue
        if(new_state in OPEN):
          #print(OPEN)
          #print(CLOSED)
          p = OPEN[new_state]
          if new_f < p:
            del OPEN[new_state]
            OPEN.insert(new_state,new_f)
            #print(OPEN)
          else:
            del new_state
            continue
        else:
          OPEN.insert(new_state,new_f)
          #print(OPEN)
          #print(CLOSED)
        BACKLINKS[new_state] = S
        g[new_state] = new_g
        #print(OPEN)
   # ***STUDENTS IMPLEMENT THE GENERATION AND HANDLING OF SUCCESSORS HERE,
   # USING THE GIVEN PRIORITY QUEUE FOR THE OPEN LIST, AND
   # DETERMINING THE SHORTEST DISTANCE KNOWN SO FAR FROM THE INITIAL STATE TO
   # EACH SUCCESSOR.***

  # STEP 6. Go to Step 2.
  return None  # No more states on OPEN, and no goal reached.

def print_state_queue(name, q):
  print(name+" is now: ",end='')
  print(str(q))

def backtrace(S):
  global BACKLINKS
  path = []
  while S:
    path.append(S)
    S = BACKLINKS[S]
  path.reverse()
  print("Solution path: ")
  for s in path:
    print(s)
  print("TOTAL_COST is:"+str(TOTAL_COST))
  print('Length of solution path found: '+str(len(path)-1)+' edges')
  return path

def report(open, closed, count):
  print("len(OPEN)="+str(len(open)), end='; ')
  print("len(CLOSED)="+str(len(closed)), end='; ')
  print("COUNT = "+str(count))

if __name__=='__main__':
  runUCS()