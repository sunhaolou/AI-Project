'''
Name(s): Haolou Sun
UW netid(s): sunhaolo
'''

from game_engine import genmoves

class BackgammonPlayer:
    def __init__(self):
        self.GenMoveInstance = genmoves.GenMoves()
        self.maxply = 2
        self.dice = [] # A list contains the output pairs of the two dices.
        for i in range(6):
            for j in range(6):
                self.dice.append((i+1, j+1))
        self.moveWithEval = {} # A dictionary contain the moves with its corresponding static eval.
        # The static eval will the keys and the moves will be the values.

    # TODO: return a string containing your UW NETID(s)
    # For students in partnership: UWNETID + " " + UWNETID
    def nickname(self):
        # TODO: return a string representation of your UW netid(s)
        return "sunhaolo guan123"

    def initialize_move_gen_for_state(self, state, who, die1, die2):
        self.move_generator = self.GenMoveInstance.gen_moves(state, who, die1, die2)

    # Given a ply, it sets a maximum for how far an agent
    # should go down in the search tree. Count the chance nodes
    # as a ply too!
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
    # the state.whose_move
    # Keep in mind: a player can only pass if the player cannot move any checker with that role
    def move(self, state, die1, die2):
        # TODO: return a move for the current state and for the current player.
        # Hint: you can get the current player with state.whose_move
        self.initialize_move_gen_for_state(state, state.whose_move, die1, die2)
        self.moveWithEval.clear()
        val = self.expectminimax(state, state.whose_move, self.maxply, die1, die2) # Get the best value
        move = self.moveWithEval[val] # Get the move that corresponding to the value
        return move


    def expectminimax(self, state, whoseMove, depth, die1, die2):
        if depth == 0: # If we reach the bottom of the search, we will return its static eval.
            return self.staticEval(state)

        # Since in our static eval function, the larger the value, the better for the white player.
        # Thus, we need to initialize a really small number when it's the White player's turn.
        # On the contrary, for the red player.
        if whoseMove == 0:
            val = -10000000000
        else:
            val = 10000000000

        move = None
        moves = self.get_all_possible_moves(state)
        for m in moves:
            expectVal = 0 # The expected value.
            for (die1, die2) in self.dice:
                # The expected value is the sum of the value of the bottom level times their
                # probability which is 1/36.
                expectVal += 1/36 * self.expectminimax(m[1], m[1].whose_move, depth - 1, die1, die2)
            # If it's the white player's turn, we will keep the larger static value.
            # If it's the red player's turn, we will keep the smaller static value.
            if (whoseMove == 0 and expectVal > val) or (whoseMove == 1 and expectVal < val):
                val = expectVal
                move = m[0]

        self.moveWithEval[val] = move # Record the move with the its static value into the dictionary.
        return val


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



    def get_all_possible_moves(self, state):
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
