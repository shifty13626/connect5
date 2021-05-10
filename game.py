from Player import Player
from state import State, BOARD_WIDTH
from colors import Colors
import time

NUMBER_OF_TURNS_BEFORE_INCREMENTING_DEPTH = 25


class Game:
    first_player = Player.IA
    state = None
    current_player = first_player

    def __init__(self, max_depth=6):
        self.max_depth = max_depth

    def start_game(self):
        turn_count = 1
        self.ask_first_player()
        while not self.state.is_terminal_state():
            if turn_count % NUMBER_OF_TURNS_BEFORE_INCREMENTING_DEPTH == 0:
                self.max_depth += 1
            # if turn player
            if self.current_player == Player.HUMAN:
                column_selected = -1
                while not self.is_valid_entry(column_selected):
                    print(Colors.HEADER.value + "C'est votre tour !" + Colors.ENDC.value)
                    # display grid
                    print(Colors.WARNING.value + ' | '.join(
                        [str(i) for i in range(0, BOARD_WIDTH)]) + Colors.ENDC.value)
                    self.state.print_board()
                    column_selected = int(input(
                        Colors.HEADER.value + "Selectionnez la colonne dans laquelle placer votre pion : " + Colors.ENDC.value))
                ai_pos, pos, heights = self.state.play_turn(column_selected, first_player=self.first_player)
                self.current_player = Player.IA
                self.state = State(ai_pos, pos, heights, current_player=self.current_player)
            # if IA
            else:
                start_time = time.time()
                self.state = self.state.get_next_move(first_player=self.first_player, max_depth=self.max_depth)
                self.current_player = Player.HUMAN
                self.state.current_player = self.current_player
                print(Colors.HEADER.value + "L'IA vient de jouer en " + str(round(time.time() - start_time, 2)) + " secondes" + Colors.ENDC.value)
            turn_count += 1
            print()
        # end game
        self.state.print_board()
        if self.state.is_winning_state(self.state.human_position):
            print(Colors.OKGREEN.value + "Vous avez gagné !" + Colors.ENDC.value)
        elif self.state.is_winning_state(self.state.ai_position):
            print(Colors.FAIL.value + "Vous avez perdu..." + Colors.ENDC.value)
        else:
            print(Colors.WARNING.value + "Égalité !" + Colors.ENDC.value)

    def is_valid_entry(self, entry):
        if entry in self.state.get_possible_moves():
            return True
        return False

    def ask_first_player(self):
        self.first_player = Player.IA if input("Voulez-vous commencer? (O/n)") == "n" else Player.HUMAN
        self.current_player = self.first_player
        self.state = State(0, 0, current_player=self.current_player)


if __name__ == '__main__':
    game = Game()
    game.start_game()
