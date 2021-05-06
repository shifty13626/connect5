import unittest

from Player import Player
from state import State, BOARD_WIDTH


class StateTest(unittest.TestCase):
    def test_winner_horizontal(self):
        # 1 1 1 1 1
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        winning_position = 0b1000000010000000100000001000000010000000   # 5 coin in last line (bottom)
        self.assertTrue(State.is_winning_state(winning_position))

    def test_no_winner_horizontal(self):
        # 1 1 0 1 1
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        winning_position = 0b1000000010000000000000001000000010000000
        self.assertFalse(State.is_winning_state(winning_position))

    def test_no_winner_horizontal_on_edge(self):
        # 0 0 0 1 1
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        winning_position = 0b0000000000000000000000001000000010000000
        self.assertFalse(State.is_winning_state(winning_position))

    def test_winner_vertical(self):
        # 0 0 0 0 1
        # 0 0 0 0 1
        # 0 0 0 0 1
        # 0 0 0 0 1
        # 0 0 0 0 1
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        winning_position = 0b0000000011111000   # 5 coin in last line (bottom)
        self.assertTrue(State.is_winning_state(winning_position))

    def test_no_winner_vertical(self):
        # 0 0 0 0 1
        # 0 0 0 0 1
        # 0 0 0 0 0
        # 0 0 0 0 1
        # 0 0 0 0 1
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        winning_position = 0b0000000011011000
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
        winning_position = 0b00010000_0000100_000000100_00000010_00000001   # 5 coin in last line (bottom)
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
        winning_position = 0b0001000000001000000000000000001000000001
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
        winning_position = 0b0000000000000000000000000000001000000001
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
        winning_position = 0b0000000100000010000001000000100000010000   # 5 coin in last line (bottom)
        self.assertTrue(State.is_winning_state(winning_position))

    def test_no_winner_diagonal_rl(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 1
        # 0 0 0 1 0
        # 0 0 0 0 0
        # 0 1 0 0 0
        # 1 0 0 0 0
        winning_position = 0b0000000100000010000000000000100000010000
        self.assertFalse(State.is_winning_state(winning_position))

    def test_is_draw(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 1
        # 0 0 0 1 0
        # 0 0 1 0 0
        # 0 1 0 0 0
        # 1 0 0 0 0
        draw_position = 0b111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        self.assertTrue(State.is_draw_state(draw_position))

    def test_is_not_draw(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 1
        # 0 0 0 1 0
        # 0 0 1 0 0
        # 0 1 0 0 0
        # 1 0 0 0 0
        draw_position = 0b111111110111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        self.assertFalse(State.is_draw_state(draw_position))

    def test_ai_turn_two_times_in_same_row(self):
        ia_position_after_move = 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000001
        state = State(0, 0)
        new_ai_position, new_game_position, new_col_heights = state.play_turn(0, first_player=Player.IA)
        self.assertEqual(ia_position_after_move, new_ai_position)

    def test_human_turn_two_times_in_same_row(self):
        human_position_after_move = 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000001
        state = State(0, 0)
        new_ai_position, new_game_position, new_col_heights = state.play_turn(0, first_player=Player.HUMAN)
        self.assertEqual(human_position_after_move, new_ai_position ^ new_game_position)

    def test_get_possible_move_empty_board(self):
        state = State(0, 0)
        expected = [i for i in range(0, BOARD_WIDTH)]
        self.assertEqual(expected, state.get_possible_moves())

    def test_get_possible_move_with_full_board(self):
        position = 0b11111111_11111111_11111111_11111111_11111111_11111111_11111111_11111111_11111111_11111111_11111111_11111111
        state = State(position, position)
        expected = []
        self.assertEqual(expected, state.get_possible_moves())

    def test_get_next_move(self):
        state = State(0, 0)
        new_state = state.get_next_move(first_player=Player.IA)
        new_state.print_board()
        new_state = new_state.get_next_move(first_player=Player.HUMAN)
        new_state.print_board()

if __name__ == '__main__':
    unittest.main()
