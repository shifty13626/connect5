BOARD_WIDTH = 12
BOARD_HEIGHT = 8

infinity = float('inf')
MAX_DEPTH = 10


class State:
    def __init__(self, ai_position, game_position):
        self.ai_position = ai_position
        self.game_position = game_position

    @property
    def human_position(self):
        return self.ai_position ^ self.game_position

    @staticmethod
    def is_winning_state(position):
        if position & (position >> (BOARD_HEIGHT - 1)) & (position >> ((BOARD_HEIGHT - 1) * 2)) & ((BOARD_HEIGHT - 1) * 3) & (position >> ((BOARD_HEIGHT - 1) * 4)) != 0:
            return True  # diagonal \
        if position & (position >> (BOARD_HEIGHT + 1)) & (position >> ((BOARD_HEIGHT + 1) * 2)) & (position >> ((BOARD_HEIGHT + 1) * 3)) & (position >> ((BOARD_HEIGHT + 1) * 4)) != 0:
            return True  # diagonal /
        if position & (position >> BOARD_HEIGHT) & (position >> (BOARD_HEIGHT * 2)) & (position >> (BOARD_HEIGHT * 3)) & (position >> (BOARD_HEIGHT * 4)) != 0:
            return True  # horizontal
        if position & (position >> 1) & (position >> 2) & (position >> 3) & (position >> 4) != 0:
            return True  # vertical
        return False

    @staticmethod
    def is_draw_state(position):
        is_draw = True
        for column in range(0, BOARD_WIDTH):
            if not (position & (1 << BOARD_HEIGHT * column + (BOARD_HEIGHT - 1))):
                is_draw = False
        return is_draw

    def is_terminal_state(self):
        if self.is_winning_state(self.ai_position):
            return True
        elif self.is_winning_state(self.human_position):
            return True
        elif self.is_draw_state(self.game_position):
            return True
        else:
            return False

    def get_heuristic(self):
        # TODO
        return 42

    def get_children(self):
        # TODO
        return self

    def print_board(self):
        ai_board, total_board = self.ai_position, self.game_position
        for row in range(BOARD_HEIGHT-1, -1, -1):
            print("")
            for column in range(0, BOARD_WIDTH):
                if ai_board & (1 << (BOARD_WIDTH * column + row)):
                    print("1 ", end='')
                elif total_board & (1 << (BOARD_WIDTH * column + row)):
                    print("2 ", end='')
                else:
                    print("0 ", end='')
        print("")

    def __hash__(self):
        return hash((self.ai_position, self.game_position))

    def __eq__(self, other):
        return (self.ai_position, self.game_position) == (
            other.ai_position, other.game_position)

    def get_next_move(self):

        def alpha_beta_pruning(ai_state, ai_alpha, ai_beta, ai_depth, ai_max_depth):
            if ai_state.is_terminal_state() or ai_depth > ai_max_depth:
                return ai_state.get_heuristic()
            if ai_depth % 2 == 0:
                w_value = infinity
                for child in ai_state.get_children():
                    if child in known_states:
                        continue
                    w_value = min(w_value, alpha_beta_pruning(child, ai_alpha, ai_beta, ai_depth + 1, ai_max_depth))
                    known_states[child] = w_value
                    if ai_alpha >= w_value:
                        return w_value
                    ai_beta = min(ai_beta, w_value)
            else:
                w_value = -infinity
                for child in ai_state.get_children():
                    if child in known_states:
                        continue
                    w_value = max(w_value, alpha_beta_pruning(child, ai_alpha, ai_beta, ai_depth + 1, ai_max_depth))
                    known_states[child] = ai_alpha
                    if w_value >= ai_beta:
                        return w_value
                    ai_alpha = min(ai_alpha, w_value)
            return w_value

        known_states = {}
        best_state = None
        best_score = -infinity
        for state in self.get_children():
            v = alpha_beta_pruning(state, -infinity, infinity, 1, MAX_DEPTH)
            if v > best_score:
                best_score = v
                best_state = state
        return best_state
