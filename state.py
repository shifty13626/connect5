from enum import Enum

from Player import Player
from colors import Colors

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
MAX_MOVE_TO_WIN = BOARD_WIDTH * BOARD_HEIGHT // 2 + 1

infinity = float('inf')
MAX_DEPTH = 9


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
                (BOARD_HEIGHT - 1) * 3) & (position >> ((BOARD_HEIGHT - 1) * 4)) != 0:
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
    def is_draw_state(position):
        is_draw = True
        # check that each column is not full
        for column in range(0, BOARD_WIDTH):
            if not (position & (1 << BOARD_HEIGHT * column + (BOARD_HEIGHT - 1))):
                is_draw = False
        return is_draw

    def is_terminal_state(self):
        if self.is_winning_state(self.ai_position):
            self.game_status = GameStatus.AI_WIN
            #self.print_board()
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
            return MAX_MOVE_TO_WIN - self.depth // 2
        elif self.game_status == GameStatus.HUMAN_WIN:
            return - (MAX_MOVE_TO_WIN - self.depth // 2)
        elif self.game_status == GameStatus.DRAW:
            return 0
        elif self.depth % 2 == 0:
            return infinity
        else:
            return -infinity

    def get_children(self, first_player):
        children = []
        for possible_move in self.get_possible_moves():
            new_ai_position, new_game_position, new_col_heights = self.play_turn(possible_move, first_player)
            new_state = State(new_ai_position, new_game_position, new_col_heights, self.depth + 1)
            children.append(new_state)
        return children

    def get_possible_moves(self):
        possible_moves = []
        for column in range(0, BOARD_WIDTH):
            # si la derniere ligne de la colonne est vide alors on l'enregistre
            if not (self.game_position & (1 << BOARD_HEIGHT * column + (BOARD_HEIGHT - 1))):
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
        for row in range(BOARD_HEIGHT - 1, -1, -1):
            print("")
            for column in range(0, BOARD_WIDTH):
                if ai_board & (1 << (BOARD_HEIGHT * column + row)):
                    print(Colors.FAIL.value + "1" + Colors.FAIL.value, end='')
                elif total_board & (1 << (BOARD_HEIGHT * column + row)):
                    print(Colors.OKGREEN.value + "2" + Colors.OKGREEN.value, end='')
                else:
                    print(Colors.OKCYAN.value + "0" + Colors.OKCYAN.value, end='')
                if 0 <= column < 11:
                    print(" | ", end='')
        print("")

    def __hash__(self):
        return hash((self.ai_position, self.game_position))

    def __eq__(self, other):
        return (self.ai_position, self.game_position) == (
            other.ai_position, other.game_position)

    def get_next_move(self, first_player):

        def alpha_beta_pruning(ai_state, ai_alpha, ai_beta, ai_max_depth):

            if ai_state.is_terminal_state() or ai_state.depth > ai_max_depth:
                node_value = ai_state.get_heuristic()
                return node_value
            if ai_state.depth % 2 == 1:
                print('min', ai_alpha, ai_beta, ai_state.depth)
                w_value = infinity
                for child in ai_state.get_children(first_player):
                    if child in known_states:
                        continue
                    alpha_beta_result = alpha_beta_pruning(child, ai_alpha, ai_beta, ai_max_depth)
                    w_value = min(w_value, alpha_beta_result)
                    known_states[child] = w_value
                    if ai_alpha >= w_value:
                        return w_value
                    ai_beta = min(ai_beta, w_value)
            else:
                print('max', ai_alpha, ai_beta, ai_state.depth)
                w_value = -infinity
                for child in ai_state.get_children(first_player):
                    if child in known_states:
                        continue
                    w_value = max(w_value, alpha_beta_pruning(child, ai_alpha, ai_beta, ai_max_depth))
                    known_states[child] = ai_alpha
                    if w_value >= ai_beta:
                        return w_value
                    ai_alpha = max(ai_alpha, w_value)
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
