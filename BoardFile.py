class Board:

    def __init__(self):
        self.b = [
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', 'W', 'B', '_', '_', '_'],
            ['_', '_', '_', 'B', 'W', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_']
        ]

    def get_scores(self):
        count_w = 0
        count_b = 0
        for i in self.b:
            for j in i:
                if j == 'W':
                    count_w += 1
                elif j == 'B':
                    count_b += 1
        return count_w, count_b

    def diplay_moves(self, board):
        for i in board:
            for j in i:
                print(j,
                      end=" ")  #the end=" " argument in the print function is used to prevent a newline character from being printed after each element, so all elements in the same row are printed on the same line.
            print()

    def show_available_moves(self, valid_moves):
        global i
        state = [row[:] for row in self.b]  # Create a copy of self.b
        counter_row = 0
        print(range(8), end=" ")
        for move in valid_moves:
            i = move[-1]
            j = move[-2]
            print(i, j)
            for row_idx, row in enumerate(state):
                for col_idx, column in enumerate(row):
                    if i == row_idx and j == col_idx:
                        state[i][j] = "O"
        print(" ", end=" ")
        for r in range(8):
            print(r, end=" ")
        print()
        for row in state:
            print(counter_row, end=" ")
            counter_row += 1
            for element in row:
                print(element, end=" ")
            print()

    def print_board(self):
        for i in self.b:

            for j in i:
                print(j,
                      end=" ")  #the end=" " argument in the print function is used to prevent a newline character from being printed after each element, so all elements in the same row are printed on the same line.
            print()
