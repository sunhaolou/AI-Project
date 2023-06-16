'''
Name(s): Longjie Guan
UW netid(s): 2272669
'''

from game_engine import genmoves

class BackgammonPlayer:
    def __init__(self):
        self.GenMoveInstance = genmoves.GenMoves()
        self.maxply = 2
        self.COUNT_STATE = 0             # count the number of states created by the agent
        self.COUNT_ABCUT = 0             # count the number of alpha-beta cutoffs
        self.prune = False
        # feel free to create more instance variables as needed.

    # TODO: return a string containing your UW NETID(s)
    # For students in partnership: UWNETID + " " + UWNETID
    def nickname(self):
        # TODO: return a string representation of your UW netid(s)
        return "2272669" + " " + "1934592"

    def initialize_move_gen_for_state(self, state, who, die1, die2):
        self.move_generator = self.GenMoveInstance.gen_moves(state, who, die1, die2) 

    # If prune==True, then your Move method should use Alpha-Beta Pruning
    # otherwise Minimax
    def useAlphaBetaPruning(self, prune=False):
        # TODO: use the prune flag to indiciate what search alg to use
        self.COUNT_STATE = 0
        self.COUNT_ABCUT = 0
        self.prune = prune

    # Returns a tuple containing the number explored
    # states as well as the number of cutoffs.
    def statesAndCutoffsCounts(self):
        # TODO: return a tuple containig states and cutoff (截止点))
        return (self.COUNT_STATE, self.COUNT_ABCUT)

    # Given a ply, it sets a maximum for how far an agent
    # should go down in the search tree. maxply=2 indicates that
    # our search level will go two level deep.
    def setMaxPly(self, maxply=2):
        # TODO: set the max ply
        if maxply != 2:
            self.maxply = maxply

    # If not None, it update the internal static evaluation
    # function to be func
    def useSpecialStaticEval(self, func):
        # TODO: update your staticEval function appropriately
        if func is not None:
            self.staticEval = func

    # Given a state and a roll of dice, it returns the best move for
    # the state.whose_move.
    # Keep in mind: a player can only pass if the player cannot move any checker with that role
    def move(self, state, die1=1, die2=6):
        # TODO: return a move for the current state and for the current player.
        # Hint: you can get the current player with state.whose_move
        self.initialize_move_gen_for_state(state, state.whose_move, die1, die2)

        # This step runs the alphabeta_prun and tries to get the count of state and cutoff
        #self.alphabete_prun(state, state.whose_move, self.maxply, -10000000000, 10000000000, die1, die2)
        #self.prune = self.useAlphaBetaPruning(False)

        #self.initialize_move_gen_for_state(state, state.whose_move, die1, die2)

        if self.prune == True:
            (alscore, optimal_almove) = self.alphabete_prun(state, state.whose_move, self.maxply, -10000000000, 10000000000, die1, die2)
            return optimal_almove
        else:
            (miscore, optimal_mimove) = self.minimax(state, state.whose_move, self.maxply, die1, die2)        # get the score of each move
            return optimal_mimove

    def minimax(self, state, whosemove, depth, die1, die2):                  # depth means how many moves ahead we want to search\
        move = None
        moves = self.get_all_possible_moves(state, die1, die2)                  # get all possible moves and states for the state in

        if depth == 0:
            return (self.staticEval(state), move)

        if whosemove == 0:                                                   # maximizer and white move
            val = -10000000000
            for m in moves:
                (valp, recumove) = self.minimax(m[1], m[1].whose_move, depth - 1, die1, die2)
                self.COUNT_STATE = self.COUNT_STATE + 1                         # visit to this state, so the state count increases
                if valp > val:
                    val = valp
                    move = m[0]
            return (val, move)
        else:                                                                # minimizer and red move
            val = 10000000000
            for m in moves:
                (valp, recumove) = self.minimax(m[1], m[1].whose_move, depth - 1, die1, die2)
                self.COUNT_STATE = self.COUNT_STATE + 1
                if valp < val:
                    val = valp
                    move = m[0]
            return (val, move)

    def alphabete_prun(self, state, whosemove, depth, a, b, die1, die2):                # this state input is the child of initial state
        move = None
        moves = self.get_all_possible_moves(state, die1, die2)                  # get all possible moves and states for the state in

        if depth == 0: # If we reach the bottom of the search, we will return its static eval.
            return (self.staticEval(state), move)

        if whosemove == 0:                                                      # maximizer
            val = -10000000000
            for m in moves:
                (valp, recumove) = self.alphabete_prun(m[1], m[1].whose_move, depth - 1, a, b, die1, die2)
                if valp > val:
                    val = valp
                    move = m[0]
                a = max(a, valp)
                if b <= a:                                                      # the cut-off occurs
                    self.COUNT_ABCUT = self.COUNT_ABCUT + 1                     # count the number of cutoff during the search
                    break
                self.COUNT_STATE = self.COUNT_STATE + 1                         # visit to this state, so the state count increases
            return (val, move)
        else:                                                                   # minimizer
            val = 10000000000
            for m in moves:
                (valp, recumove) = self.alphabete_prun(m[1], m[1].whose_move, depth - 1, a, b, die1, die2)
                if valp < val:
                    val = valp
                    move = m[0]
                b = min(b, valp)
                if b <= a:
                    self.COUNT_ABCUT = self.COUNT_ABCUT + 1
                    break
                self.COUNT_STATE = self.COUNT_STATE + 1                         # visit to this state, so the state count increases
            return (val, move)

    def get_all_possible_moves(self, state, die1, die2):
        """Uses the mover to generate all legal moves. Returns an array of move commands"""
        move_list = []
        done_finding_moves = False
        any_non_pass_moves = False
        while not done_finding_moves:
            try:
                m = next(self.move_generator)    # Gets a (move, state) pair.
                # print("next returns: ",m[0]) # Prints out the move.    For debugging.
                if m[0] != 'p':
                    any_non_pass_moves = True
                    move_list.append(m)    # Add the (move, state) to the list.
            except StopIteration as e:
                done_finding_moves = True
        if not any_non_pass_moves:
            move_list.append(('p', state))
        return move_list

    # Hint: Look at game_engine/boardState.py for a board state properties you can use.
    def staticEval(self, state):
        # TODO: return a number for the given state
        eval_list = state.pointLists
        white_score = 0
        red_score = 0
        for i in range(24):
            if len(eval_list[i]) > 0:
                if eval_list[i][0] == 0:
                    if len(eval_list[i]) == 2:
                        white_score += 2*(i+1)
                    elif len(eval_list[i]) == 3:
                        white_score += 4*(i+1)
                    elif len(eval_list[i]) == 4:
                        white_score += 8*(i+1)
                    elif len(eval_list[i]) == 5:
                        white_score += 10*(i+1)
                    elif len(eval_list[i]) == 1:
                        white_score += 1*(i+1)
                if eval_list[i][0] == 1:
                    if len(eval_list[i]) == 2:
                        red_score += 2*(i+1)
                    elif len(eval_list[i]) == 3:
                        red_score += 4*(i+1)
                    elif len(eval_list[i]) == 4:
                        red_score += 8*(i+1)
                    elif len(eval_list[i]) == 5:
                        red_score += 10*(i+1)
                    elif len(eval_list[i]) == 1:
                        red_score += 1*(i+1)
        if len(state.white_off) != 0:
            white_score += 100*len(state.white_off)
        if len(state.red_off) != 0:
            red_score += 100*len(state.red_off)
        return white_score - red_score