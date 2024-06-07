import copy
import math
from PlayerFile import Player


class AIagent(Player):

    def __init__(self, level):
        self.level = level
        super().__init__('W')
        self.ref_disks = 30

    def terminal(self, state, refdisks, opponentdisks):
        #first case: no empty cell
        for i in state:
            for j in i:
                if j == '_':
                    return False

        #second case: no avaliable disks
        if refdisks == 0 or opponentdisks == 0:
            return True

        return False

    def evaluate(self, state):
        count = 0
        for i in state:
            for j in i:
                if j == 'W':
                    count += 1
        return count


    def alpha_beta(self, state, depth, alpha, beta, maximizingPlayer, opponentdisks):
        if depth == 0 or self.terminal(state, self.ref_disks, opponentdisks):
            return self.evaluate(state), None  # Return the evaluation value and None for the move

        best_move = None  # Variable to store the best move
        if maximizingPlayer:
            best_value = -math.inf
            moves = super().generate_moves(state, maximizingPlayer)
            if not moves:
                # pass turn without playing
                value, _ = self.alpha_beta(state, depth - 1, alpha, beta, False, opponentdisks)
                return value, None  # Return the value and None for the move

            for move in moves:
                new_state = self.apply_move(state, move, maximizingPlayer)
                value, _ = self.alpha_beta(new_state, depth - 1, alpha, beta, False, opponentdisks)
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, best_value)
                if alpha >= beta:
                    break
            self.ref_disks -= 1
            return best_value, best_move

        else:
            best_value = math.inf
            moves = super().generate_moves(state, maximizingPlayer)
            if not moves:
                # pass turn without playing
                value, _ = self.alpha_beta(state, depth - 1, alpha, beta, True, opponentdisks)
                return value, None  # Return the value and None for the move

            for move in moves:
                new_state = self.apply_move(state, move, maximizingPlayer)
                value, _ = self.alpha_beta(new_state, depth - 1, alpha, beta, True, opponentdisks - 1)
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, best_value)
                if alpha >= beta:
                    break
            return best_value, best_move

    def make_move(self, state, level, opponentdisks):
        # ignore the evaluation value (first return)
        self.ref_disks = copy.deepcopy(self.disks)  # Create a deep copy of self.disks
        ref_state = [row[:] for row in state]  # Create a copy of self.b
        _, move = self.alpha_beta(ref_state, level, -math.inf, math.inf, True, opponentdisks)
        return move
