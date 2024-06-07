from AIagentFile import AIagent
from GameFile import Game
from PlayerFile import Player


def main():
    depth = 0
    player = Player('B')
    x = int(input("please choose your level\n1-easy\n2-medium\n3-hard "))
    if x == 1:
        depth = 1
    elif x == 2:
        depth = 3
    elif x == 3:
        depth = 5

    computer = AIagent(depth)

    game = Game(player, computer, x)
    game.start_game()


main()

