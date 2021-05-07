from enum import Enum

from Player import Player
from colors import Colors

BOARD_WIDTH = 12
BOARD_HEIGHT = 9
MAX_MOVE_TO_WIN = (BOARD_WIDTH * (BOARD_HEIGHT - 1) // 2 + 1) + 10000

infinity = float('inf')
MAX_DEPTH = 6

heuristic_values = [
    3,  4,  5,  6,  6,  5,  4, 3,
    4,  6,  7,  9,  9,  7,  6, 4,
    5,  7, 10, 12, 12, 10,  7, 5,
    6,  9, 13, 14, 14, 13,  9, 6,
    8, 11, 14, 16, 16, 14, 11, 8,
    8, 11, 14, 16, 16, 14, 11, 8,
    8, 11, 14, 16, 16, 14, 11, 8,
    8, 11, 14, 16, 16, 14, 11, 8,
    6,  9, 13, 14, 14, 13,  9, 6,
    5,  7, 10, 12, 12, 10,  7, 5,
    4,  6,  7,  9,  9,  7,  6, 4,
    3,  4,  5,  6,  6,  5,  4, 3,
]


class GameStatus(Enum):
    AI_WIN = -1
    HUMAN_WIN = 1
    DRAW = 0
    NOT_ENDED = 2


class State:
    game_status = GameStatus.NOT_ENDED

    def __init__(self, ai_position, game_position, col_heights=None, depth=0):
        if col_heights is None:
            col_heights = [i * BOARD_HEIGHT for i in range(0, BOARD_WIDTH)]
        self.ai_position = ai_position
        self.game_position = game_position
        self.depth = depth
        self.col_heights = col_heights

    @property
    def human_position(self):
        return self.ai_position ^ self.game_position

    @staticmethod
    def is_winning_state(position):
        if position & (position >> (BOARD_HEIGHT - 1)) & (position >> ((BOARD_HEIGHT - 1) * 2)) & (
                position >> (BOARD_HEIGHT - 1) * 3) & (position >> ((BOARD_HEIGHT - 1) * 4)) != 0:
            return True  # diagonal \
        if position & (position >> (BOARD_HEIGHT + 1)) & (position >> ((BOARD_HEIGHT + 1) * 2)) & (
                position >> ((BOARD_HEIGHT + 1) * 3)) & (position >> ((BOARD_HEIGHT + 1) * 4)) != 0:
            return True  # diagonal /
        if position & (position >> BOARD_HEIGHT) & (position >> (BOARD_HEIGHT * 2)) & (
                position >> (BOARD_HEIGHT * 3)) & (position >> (BOARD_HEIGHT * 4)) != 0:
            return True  # horizontal
        if position & (position >> 1) & (position >> 2) & (position >> 3) & (position >> 4) != 0:
            return True  # vertical
        return False

    @staticmethod
    def get_score_four(position):
        score = 0
        if position & (position >> (BOARD_HEIGHT - 1)) & (position >> ((BOARD_HEIGHT - 1) * 2)) & (
                (BOARD_HEIGHT - 1) * 3) != 0:
            score += 8
        if position & (position >> (BOARD_HEIGHT + 1)) & (position >> ((BOARD_HEIGHT + 1) * 2)) & (
                position >> ((BOARD_HEIGHT + 1) * 3)) != 0:
            score += 8
        if position & (position >> BOARD_HEIGHT) & (position >> (BOARD_HEIGHT * 2)) & (
                position >> (BOARD_HEIGHT * 3)) != 0:
            score += 8
        if position & (position >> 1) & (position >> 2) & (position >> 3) != 0:
            score += 8
        return score

    @staticmethod
    def get_score_three(position):
        score = 0
        if position & (position >> (BOARD_HEIGHT - 1)) & (position >> ((BOARD_HEIGHT - 1) * 2)) != 0:
            score += 2
        if position & (position >> (BOARD_HEIGHT + 1)) & (position >> ((BOARD_HEIGHT + 1) * 2)) != 0:
            score += 2
        if position & (position >> BOARD_HEIGHT) & (position >> (BOARD_HEIGHT * 2)) != 0:
            score += 2
        if position & (position >> 1) & (position >> 2) != 0:
            score += 2
        return score

    @staticmethod
    def is_draw_state(position):
        is_draw = True
        # check that each column is not full
        for column in range(0, BOARD_WIDTH):
            if not (position & (1 << BOARD_HEIGHT * column + (BOARD_HEIGHT - 2))):
                is_draw = False
        return is_draw

    def is_terminal_state(self):
        if self.is_winning_state(self.ai_position):
            self.game_status = GameStatus.AI_WIN
            # self.print_board()
            return True
        elif self.is_winning_state(self.human_position):
            self.game_status = GameStatus.HUMAN_WIN
            return True
        elif self.is_draw_state(self.game_position):
            self.game_status = GameStatus.DRAW
            return True
        else:
            return False

    def get_heuristic(self):
        if self.game_status == GameStatus.AI_WIN:
            return infinity
        elif self.game_status == GameStatus.HUMAN_WIN:
            return -infinity
        elif self.game_status == GameStatus.DRAW:
            return 0
        elif self.depth % 2 == 0:
            # return MAX_MOVE_TO_WIN - self.depth
            return self.get_score_four(self.ai_position) + self.get_score_three(self.ai_position) - (
                        self.get_score_four(self.human_position) + self.get_score_three(self.human_position))
        else:
            # return - (MAX_MOVE_TO_WIN - self.depth)
            return - (self.get_score_four(self.human_position) + self.get_score_three(self.human_position)) + (
                        self.get_score_four(self.ai_position) + self.get_score_three(self.ai_position))

    def get_children(self, first_player):
        children = []
        for possible_move in self.get_possible_moves():
            new_ai_position, new_game_position, new_col_heights = self.play_turn(possible_move, first_player)
            new_state = State(new_ai_position, new_game_position, new_col_heights, self.depth + 1)
            children.append(new_state)
        return children

    @staticmethod
    def get_heuristic_values():
        length = BOARD_WIDTH * BOARD_HEIGHT
        heuristic_values = [0] * length
        # Column
        for col in range(0, BOARD_WIDTH):
            for row in range(0, BOARD_HEIGHT - 5):
                for i in range(0, 5):
                    heuristic_values[col * BOARD_HEIGHT + row + i] += 1
        # Row
        for row in range(0, BOARD_HEIGHT - 1):
            for col in range(0, BOARD_WIDTH - 5 + 1):
                for i in range(0, 5):
                    heuristic_values[col * BOARD_HEIGHT + row + i * BOARD_HEIGHT] += 1
        return heuristic_values
        # Diagonals

    def get_heuristic_v2(self):
        if self.game_status == GameStatus.AI_WIN:
            return infinity
        elif self.game_status == GameStatus.HUMAN_WIN:
            return - infinity
        elif self.game_status == GameStatus.DRAW:
            return 0
        else:
            length = BOARD_WIDTH * (BOARD_HEIGHT - 1)
            ai_score = 0
            human_score = 0
            for key, value in enumerate(heuristic_values):
                shift = length - key - 1
                # ai_score += ((self.ai_position & (1 << shift)) >> shift) * value
                # human_score += ((self.human_position & (1 << shift))  >> shift) * value
                ai_score += ((self.ai_position >> shift) & 1) * value
                human_score += ((self.human_position >> shift) & 1) * value
            return ai_score - human_score

    def get_heuristic_v3(self):
        if self.game_status == GameStatus.AI_WIN:
            return MAX_MOVE_TO_WIN - self.depth
        elif self.game_status == GameStatus.HUMAN_WIN:
            return - (MAX_MOVE_TO_WIN - self.depth)
        elif self.game_status == GameStatus.DRAW:
            return 0
        else:
            length = BOARD_WIDTH * (BOARD_HEIGHT - 1)
            ai_score = 0
            human_score = 0
            for key, value in enumerate(heuristic_values):
                shift = length - key - 1
                # ai_score += ((self.ai_position & (1 << shift)) >> shift) * value
                # human_score += ((self.human_position & (1 << shift))  >> shift) * value
                ai_score += ((self.ai_position >> shift) & 1) * value
                human_score += ((self.human_position >> shift) & 1) * value
            return ai_score - human_score

    def get_possible_moves(self):
        possible_moves = []
        for column in range(0, BOARD_WIDTH):
            # si la derniere ligne de la colonne est vide alors on l'enregistre
            if not (self.game_position & (1 << BOARD_HEIGHT * column + (BOARD_HEIGHT - 2))):
                possible_moves.append(column)
        return possible_moves

    def play_turn(self, col, first_player):
        token = 1 << self.col_heights[col]
        new_col_heights = self.col_heights.copy()
        new_col_heights[col] += 1
        new_game_position = self.game_position ^ token
        new_ai_position = self.ai_position
        if (first_player == Player.IA and self.depth % 2 == 0) or (
                first_player == Player.HUMAN and self.depth % 2 == 1):
            new_ai_position ^= token
        return new_ai_position, new_game_position, new_col_heights

    def print_board(self):
        ai_board, total_board = self.ai_position, self.game_position
        print("0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
        for row in range(BOARD_HEIGHT - 2, -1, -1):
            for column in range(0, BOARD_WIDTH):
                if ai_board & (1 << (BOARD_HEIGHT * column + row)):
                    print(Colors.FAIL.value + "1" + Colors.FAIL.value, end='')
                elif total_board & (1 << (BOARD_HEIGHT * column + row)):
                    print(Colors.OKGREEN.value + "2" + Colors.OKGREEN.value, end='')
                else:
                    print(Colors.OKCYAN.value + "0" + Colors.OKCYAN.value, end='')
                if 0 <= column < 11:
                    print(Colors.OKCYAN.value + " | " + Colors.OKCYAN.value, end='')
            print()

    def __hash__(self):
        return hash((self.ai_position, self.game_position))

    def __eq__(self, other):
        return (self.ai_position, self.game_position) == (
            other.ai_position, other.game_position)

    def get_next_move(self, first_player):

        def alpha_beta_pruning(ai_state, ai_alpha, ai_beta, ai_max_depth):

            if ai_state.is_terminal_state() or ai_state.depth > ai_max_depth:
                node_value = ai_state.get_heuristic_v3()
                return node_value
            # MinimizingPlayer
            if ai_state.depth % 2 == 1:
                w_value = infinity
                for child in ai_state.get_children(first_player):
                    if child not in known_states:
                        w_value = min(w_value, alpha_beta_pruning(child, ai_alpha, ai_beta, ai_max_depth))
                        known_states[child] = w_value
                    else:
                        w_value = known_states[child]
                    ai_beta = min(ai_beta, w_value)
                    if ai_alpha >= ai_beta:
                        break
                return w_value

            # MaximizingPlayer
            else:
                w_value = -infinity
                for child in ai_state.get_children(first_player):
                    if child not in known_states:
                        w_value = max(w_value, alpha_beta_pruning(child, ai_alpha, ai_beta, ai_max_depth))
                        known_states[child] = w_value
                    else:
                        w_value = known_states[child]
                    ai_alpha = max(ai_alpha, w_value)
                    if ai_alpha >= ai_beta:
                        break
                return w_value

        self.depth = 0
        known_states = {}
        best_state = None
        best_score = -infinity
        for state in self.get_children(first_player):
            v = alpha_beta_pruning(state, -infinity, infinity, MAX_DEPTH)
            if v >= best_score:
                best_score = v
                best_state = state
        print(len(known_states))
        return best_state
