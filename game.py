from enum import Enum
from state import State
from colors import Colors

BOARD_WIDTH = 12
BOARD_HEIGHT = 8


class Player(Enum):
    PLAYER = -1
    IA = 1


class Game:
    def start_game(self):
        # Select first player
        current_player = Player.IA if input(Colors.HEADER.value +"Voulez-vous commencer? (O/n)" +Colors.HEADER.value) == "n" else Player.PLAYER
        print(Colors.HEADER.value +"Vous êtes le " + ("J1" if current_player == Player.PLAYER else "J2") +Colors.HEADER.value)

        state = State(0, 0)

        while True:
            # if turn player
            if current_player == Player.PLAYER:
                # entry player
                column_selected = 0
                entry = False
                while (not entry):
                    print(Colors.HEADER.value + "C'est votre tour !" + Colors.HEADER.value)
                    # display grid
                    print(Colors.WARNING.value + "1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12" + Colors.WARNING.value)
                    state.print_board()
                    column_selected = int(input(Colors.HEADER.value +"Selectionnez la colonne dans laquelle placer votre pion : " +Colors.HEADER.value))
                    if column_selected >= 1 and column_selected <= 12:
                        column_selected = column_selected - 1
                        entry = True

                current_player = Player.IA
            # if IA
            else:
                print(Colors.HEADER.value + "L'IA vient de jouer" +Colors.HEADER.value)
                current_player = Player.PLAYER


