from typing import Any


class Player:

    def __init__(self, color):
        self.score = 2
        self.color = color
        self.disks = 30

    def get_disks(self):
        return self.disks

    def get_score(self):
        return self.score

    def decrement_disks(self):
        self.disks -= 1

    def update_score(self, score):
        self.score = score

    # get available moves
    def valid_horizontally_right(self, state, color, opponent_color, found, i, j):
        if j >= 8 or j < 0:
            return False

        elif state[i][j] == '_':
            return False

        elif state[i][j] == color and found == True:
            return True
        elif state[i][j] == opponent_color:
            found = True
            return self.valid_horizontally_right(state, color, opponent_color, found, i, j + 1)
        return False

    def valid_horizontally_left(self, state, color, opponent_color, found, i, j):
        if j >= 8 or j < 0:
            return False
        elif state[i][j] == '_':
            return False
        elif state[i][j] == color and found == True:
            return True
        elif state[i][j] == opponent_color:
            found = True
            return self.valid_horizontally_left(state, color, opponent_color, found, i, j - 1)
        return False

    def valid_vertically_up(self, state, color, opponent_color, found, i, j):

        if i >= 8 or i < 0:
            return False
        elif state[i][j] == '_':
            return False
        elif state[i][j] == color and found == True:
            print("uv")
            return True
        elif state[i][j] == opponent_color:
            found = True
            return self.valid_vertically_up(state, color, opponent_color, found, i - 1, j)
        return False

    def valid_vertically_down(self, state, color, opponent_color, found, i, j):
        if i >= 8 or i < 0:
            return False
        elif state[i][j] == '_':
            return False
        elif state[i][j] == color and found == True:
            return True
        elif state[i][j] == opponent_color:
            found = True
            return self.valid_vertically_down(state, color, opponent_color, found, i + 1, j)
        return False

    def generate_moves(self, state, player):
        valid_moves = []
        empty = '_'
        if player:
            # generate move to white
            for i in range(8):
                valid_state = []
                for j in range(8):
                    if state[i][j] == empty:
                        #print(i, j)

                        if self.valid_vertically_up(state, 'W', 'B', False, i - 1, j):
                            print("vertically up")
                            print(i, j)
                            valid_state.append('vertically_up')
                            print("vu")

                        if self.valid_vertically_down(state, 'W', 'B', False, i + 1, j):
                            valid_state.append('vertically_down')
                            print(i, j)
                            print("vd")

                        if self.valid_horizontally_right(state, 'W', 'B', False, i, j + 1):
                            valid_state.append('horizontally_right')
                            print(i, j)
                            print("hr")

                        if self.valid_horizontally_left(state, 'W', 'B', False, i, j - 1):
                            valid_state.append('horizontally_left')
                            print(i, j)
                            print("hl")

                        if valid_state:
                            valid_state.append(j)
                            valid_state.append(i)

                            valid_moves.append(valid_state)
                            valid_state = []
        else:
            # generate move to white
            for i in range(8):
                valid_state = []
                for j in range(8):
                    if state[i][j] == empty:
                        #print(i, j)
                        if self.valid_vertically_up(state, 'B', 'W', False, i - 1, j):
                            print("vertically_up")
                            valid_state.append('vertically_up')
                            print("vu")

                        if self.valid_vertically_down(state, 'B', 'W', False, i + 1, j):
                            valid_state.append('vertically_down')
                            print("vd")
                        if self.valid_horizontally_right(state, 'B', 'W', False, i, j + 1):
                            valid_state.append('horizontally_right')
                            print("hr")

                        if self.valid_horizontally_left(state, 'B', 'W', False, i, j - 1):
                            valid_state.append('horizontally_left')
                            print("hl")

                        if len(valid_state):
                            valid_state.append(j)
                            valid_state.append(i)
                            print(valid_state)

                            valid_moves.append(valid_state)
                            valid_state = []
        #print(valid_moves)
        return valid_moves

    def apply_vertically_up(self, state, i, j, color):
        row = i - 1
        col = j
        state[i][j] = color
        while row > 0 and state[row][col] != color:
            state[row][col] = color
            row -= 1

    def apply_horizontally_right(self, state, i, j, color):
        row = i
        col = j + 1
        state[i][j] = color
        while col < 8 and state[row][col] != color:
            state[row][col] = color
            col += 1

    def apply_horizontally_left(self, state, i, j, color):
        row = i
        col = j - 1
        state[i][j] = color
        while col > 0 and state[row][col] != color:
            state[row][col] = color
            col -= 1

    def apply_vertically_down(self, state, i, j, color):
        row = i + 1
        col = j
        state[i][j] = color
        while row < 8 and state[row][col] != color:
            state[row][col] = color
            row += 1

    def apply_move(self, state, move, player):
        if move:
            row = move[-1]
            col = move[-2]
            # as we already have the last two indexes as coordinates
            length = len(move) - 2
            i = 0
            if player:
                color = 'W'
            else:
                color = 'B'

            while i != length:
                if move[i] == 'vertically_up':
                    self.apply_vertically_up(state, row, col, color)
                elif move[i] == 'vertically_down':
                    self.apply_vertically_down(state, row, col, color)
                elif move[i] == 'horizontally_right':
                    self.apply_horizontally_right(state, row, col, color)
                elif move[i] == 'horizontally_left':
                    self.apply_horizontally_left(state, row, col, color)
                i += 1
        return state
