from state import State
from game import Game


'''
state = State(0, 0)
# print(state.player_position)

test = 0b10000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000010000000000000000000000000000000000001

test2 = test << 10
# print(bin(test2))

state.print_board()
'''

if __name__ == '__main__':
    game = Game()
    game.start_game()
