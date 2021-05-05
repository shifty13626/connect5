import unittest

from state import State


class StateTest(unittest.TestCase):
    def test_winner_horizontal(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 1 1 1 1 1
        winning_position = 0b1000000010000000100000001000000010000000   # 5 coin in last line (bottom)
        self.assertTrue(State.is_winning_state(winning_position))

    def test_no_winner_horizontal(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 1 1 0 1 1
        winning_position = 0b1000000010000000000000001000000010000000
        self.assertFalse(State.is_winning_state(winning_position))

    def test_no_winner_horizontal_on_edge(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 1 1
        winning_position = 0b0000000000000000000000001000000010000000
        self.assertFalse(State.is_winning_state(winning_position))

    def test_winner_vertical(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 1 0 0 0
        # 0 1 0 0 0
        # 0 1 0 0 0
        # 0 1 0 0 0
        # 0 1 0 0 0
        winning_position = 0b0000000011111000   # 5 coin in last line (bottom)
        self.assertTrue(State.is_winning_state(winning_position))

    def test_no_winner_vertical(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 1 0 0 0
        # 0 1 0 0 0
        # 0 0 0 0 0
        # 0 1 0 0 0
        # 0 1 0 0 0
        winning_position = 0b0000000011111000
        self.assertFalse(State.is_winning_state(winning_position))

    def test_winner_diagonal_lr(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 1 0 0 0 0
        # 0 1 0 0 0
        # 0 0 1 0 0
        # 0 0 0 1 0
        # 0 0 0 0 1
        winning_position = 0b0000100000010000001000000100000010000000   # 5 coin in last line (bottom)
        self.assertTrue(State.is_winning_state(winning_position))

    def test_no_winner_diagonal_lr(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 1 0 0 0 0
        # 0 1 0 0 0
        # 0 0 0 0 0
        # 0 0 0 1 0
        # 0 0 0 0 1
        winning_position = 0b0000100000010000000000000100000010000000
        self.assertFalse(State.is_winning_state(winning_position))

    def test_winner_diagonal_lr_on_edge(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 1 0
        # 0 0 0 0 1
        winning_position = 0b0000000000000000000000000100000010000000
        self.assertFalse(State.is_winning_state(winning_position))

    def test_winner_diagonal_rl(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 1
        # 0 0 0 1 0
        # 0 0 1 0 0
        # 0 1 0 0 0
        # 1 0 0 0 0
        winning_position = 0b1000000001000000001000000001000000001000   # 5 coin in last line (bottom)
        self.assertTrue(State.is_winning_state(winning_position))

    def test_no_winner_diagonal_rl(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 1
        # 0 0 0 1 0
        # 0 0 1 0 0
        # 0 1 0 0 0
        # 1 0 0 0 0
        winning_position = 0b1000000001000000000000000001000000001000
        self.assertFalse(State.is_winning_state(winning_position))


#     def test_conversion(self):
#         board_matrix = [[0 for x in range(w)] for y in range(h)]
#         get_bit_board(board_matrix)
#
# def get_bit_board(matrice):
#     print(matrice)

if __name__ == '__main__':
    unittest.main()
