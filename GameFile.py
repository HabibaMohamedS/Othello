import copy

from BoardFile import Board
from PlayerFile import Player


class Game:
    def __init__(self, player, computer, level):
        self.board = Board()
        self.playerH = player
        self.playerC = computer
        self.level = level

    def human_turn(self, valid):
        print(valid)
        self.board.show_available_moves(valid)

        row = int(input("please choose row of your move: "))
        col = int(input("please choose column of your move: "))
        move = validate_move(valid, row, col)
        while not move:
            new_row = int(input("please choose row of your move: "))
            new_col = int(input("please choose column of your move: "))
            move = validate_move(valid, new_row, new_col)
        self.playerH.apply_move(self.board.b, move, False)
        self.playerH.decrement_disks()
        score_w, score_b = self.board.get_scores()
        self.playerH.update_score(score_w)
        self.playerC.update_score(score_b)
        print("white score: ", score_w, "black score: ", score_b)
        self.board.print_board()

    def computer_turn(self):
        human_disks = copy.deepcopy(self.playerH.get_disks())
        computer_move = self.playerC.make_move(self.board.b, self.level, human_disks)
        print(computer_move)
        if not computer_move:
            return
        self.playerC.apply_move(self.board.b, computer_move, True)
        self.playerC.decrement_disks()
        score_w, score_b = self.board.get_scores()
        self.playerH.update_score(score_w)
        self.playerC.update_score(score_b)
        print("white score: ", score_w, "black score: ", score_b)
        self.board.print_board()

    def start_game(self):
        human_turn = True
        terminate = False
        while not terminate:
            empty = False
            for i in self.board.b:
                for j in i:
                    if j == '_':
                        empty = True
                        break
            if not empty:
                terminate = True
            else:
                #self.board.print_board()
                if human_turn:
                    print("human turn")
                    print("human print", self.playerH.get_disks())
                    valid = self.playerH.generate_moves(self.board.b, False)
                    if valid:
                        self.human_turn(valid)
                        if self.playerH.get_disks() == 0:
                            terminate = True
                    human_turn = False
                else:
                    print("computer turn")
                    print("computer print", self.playerC.get_disks())
                    self.computer_turn()
                    if self.playerC.get_disks() == 0:
                        terminate = True
                    human_turn = True
        if terminate:
            score_w, score_b = self.board.get_scores()
            print("End of Game")
            if score_b > score_w:
                print("winner is : Black")
            elif score_b < score_w:
                print("winner is : White")
            else:
                print("draw")
            #break
        #self.board.diplay_moves(stat)


def validate_move(valid, row, col):
    for move in valid:
        if move[-2] == col and move[-1] == row:
            return move
        else:
            print("error")
    return []
