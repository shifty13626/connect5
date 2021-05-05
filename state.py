BOARD_WIDTH = 12
BOARD_HEIGHT = 8


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

    # def alpha_beta_pruning(self, alpha, beta, depth, max_depth):
    #     if self.is_terminal_state() or depth > max_depth:
    #         return self.get_heuristic()
    #     if depth % 2 == 0:
    #         for child in self.get_children():


       # else:

# evaluate (node, alpha, beta)
#      if node is a leaf
#         return the utility value of node
#      if node is a minimizing node
#         for each child of node
#             beta = min (beta, evaluate (child, alpha, beta))
#             if beta <= alpha
#                 return beta
#             return beta
#      if node is a maximizing node
#         for each child of node
#             alpha = max (alpha, evaluate (child, alpha, beta))
#             if beta <= alpha
#                 return alpha
#             return alpha

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
