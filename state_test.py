import unittest
import winsound
from Player import Player
from state import State, BOARD_WIDTH, BOARD_HEIGHT


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
        winning_position = 0b000000000_000000010_000000010_000000010_000000010_000000010_000000000_000000000   # 5 coin in last line (bottom)
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
        winning_position = 0b000000010_000000010_000000000_000000010_000000010_000000010_000000000_000000000
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
        winning_position = 0b000000010_000000010_000000000_000000000_000000000_000000010_000000010_000000010
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
        winning_position = 0b000000000_000000000_000011111_000000000_000000000_000000000_000000000_000000000   # 5 coin in last line (bottom)
        self.assertTrue(State.is_winning_state(winning_position))

    def test_no_winner_vertical(self):
        # 1 0 0 0 1
        # 1 0 0 0 1
        # 0 0 0 0 0
        # 0 0 0 0 1
        # 0 0 0 0 1
        # 0 1 0 0 0
        # 0 1 0 0 0
        # 0 1 0 0 0
        winning_position = 0b000000000_000000000_000000011_011100000_000000000_000000000_000000000_000000000
        self.assertFalse(State.is_winning_state(winning_position))

    def test_winner_diagonal_lr(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 1 0 0 0 0
        # 0 1 0 0 0
        # 0 0 1 0 0
        # 0 0 0 1 0
        # 0 0 0 0 1
        position = 0b000000000_000000001_000000010_000000100_000001000_000010000_000000000_000000000
        self.assertTrue(State.is_winning_state(position))

    def test_no_winner_diagonal_lr(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 1 0 0 0 0
        # 0 1 0 0 0
        # 0 0 0 0 0
        # 0 0 0 1 0
        # 0 0 0 0 1
        winning_position = 0b000000000_000010000_000001000_000000000_000000010_000000001_000000000_000000000
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
        winning_position = 0b000000001_000000010_000000000_000000000_000000000_000000000_000000000_000000000
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
        winning_position = 0b000000000_000010000_000001000_000000100_000000010_000000001_000000000_000000000   # 5 coin in last line (bottom)
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
        winning_position = 0b000000000_000010000_000001000_000000000_000000010_000000001_000000000_000000000
        self.assertFalse(State.is_winning_state(winning_position))

    def test_is_draw(self):
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        draw_position = 0b011111111_011111111_011111111_011111111_011111111_011111111_011111111_011111111
        self.assertTrue(State.is_draw_state(draw_position))

    def test_is_not_draw(self):
        # 1 0 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        draw_position = 0b011111111_011111111_001111111_011111111_011111111_011111111_011111111_011111111
        self.assertFalse(State.is_draw_state(draw_position))

    def test_is_terminal_state_when_winning(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 1
        # 0 0 0 1 0
        # 0 0 1 0 0
        # 0 1 0 0 0
        # 1 0 0 0 0
        winning_position = 0b000000001000000010000000100000001000000010000
        state = State(ai_position=0, game_position=winning_position)
        self.assertTrue(state.is_terminal_state())

    def test_is_terminal_state_when_not_winning(self):
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 0
        # 0 0 0 0 1
        # 0 0 0 1 0
        # 0 0 0 0 0
        # 0 1 0 0 0
        # 1 0 0 0 0
        winning_position = 0b0000000100000010000000000000100000010000
        state = State(ai_position=0, game_position=winning_position)
        self.assertFalse(state.is_terminal_state())
        
    def test_is_terminal_state_when_draw(self):
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 1 1 1 1 1
        winning_position = 0b011111111_011111111_011111111_011111111_011111111_011111111_011111111_011111111
        state = State(ai_position=0, game_position=winning_position)
        self.assertTrue(state.is_terminal_state())

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
        for i in range(0, 8*8//2 - 1):
            state.print_board()
            if state.is_terminal_state():
                break
            state = state.get_next_move(first_player=Player.IA)

            state.print_board()
            if state.is_terminal_state():
                break
            ai_pos, pos, heights = state.play_turn(int(input("a toi")), first_player=Player.IA)
            state = State(ai_pos, pos, heights)
            # if state.is_terminal_state():
            #     break
            # state = state.get_next_move(first_player=Player.IA)
            # state.print_board()
            # print(bin(state.ai_position))

            # print('\a')


    @unittest.skip("just for demo")
    def test_get_heuristic_values(self):
        #0 9 18 27 36 45 54 63
        hv = State.get_heuristic_values()
        for line in range(BOARD_HEIGHT):
            for column in range(BOARD_WIDTH):
                print(hv[line + column * BOARD_HEIGHT], end='')
                if 0 < column < BOARD_WIDTH:
                    print(" | ", end='')
            print()


if __name__ == '__main__':
    unittest.main()
