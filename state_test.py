import unittest

from state import State


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
        state.play_turn(0, ai_turn=True)
        self.assertEqual(ia_position_after_move, state.ai_position)
        position_after_second_move = 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000001_00000001
        state.play_turn(1, ai_turn=True)
        self.assertEqual(position_after_second_move, state.ai_position)

    def test_play_turn_two_times_in_same_column(self):
        ia_position_after_move = 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000011
        state = State(0, 0)
        state.play_turn(0, ai_turn=True)
        state.play_turn(0, ai_turn=True)
        self.assertEqual(ia_position_after_move, state.ai_position)

    def test_human_turn_two_times_in_same_row(self):
        human_position_after_move = 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000001
        state = State(0, 0)
        state.play_turn(0, ai_turn=False)
        self.assertEqual(human_position_after_move, state.human_position)
        position_after_second_move = 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000001_00000001
        state.play_turn(1, ai_turn=False)
        self.assertEqual(position_after_second_move, state.human_position)

    def test_human_turn_two_times_in_same_column(self):
        human_position_after_move = 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000011
        state = State(0, 0)
        state.play_turn(0, ai_turn=False)
        state.play_turn(0, ai_turn=False)
        self.assertEqual(human_position_after_move, state.human_position)


if __name__ == '__main__':
    unittest.main()
