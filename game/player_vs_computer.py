from game.state import StateInterface
from game.ui.console_ui import ConsoleUI
from rock_paper_scissors.tally import Tally
from game.utils import get_player_hand, get_computer_hand
from game.game_over_state import GameOverState


class PlayerVsComputer(StateInterface):
    """Instantiated when game is started in player vs computer mode and the game would be in this state till all rounds
    are completed"""

    def __init__(self, ui: ConsoleUI):
        self._ui = ui
        self._tally = Tally(3)

    def run(self) -> StateInterface:
        self._ui.write(
            "Current Round:{0}".format(4 - self._tally.remaining_nr_of_rounds)
        )

        self._ui.write("\nSelect from")
        self._tally.hand_p1 = get_player_hand(self._ui)

        self._tally.hand_p2 = get_computer_hand()

        self._print_players_hand_selections(
            self._tally.hand_p1.name(), self._tally.hand_p2.name()
        )

        self._tally.update()
        self._print_players_scores()

        if self._tally.remaining_nr_of_rounds == 0:
            self._print_game_result(self._tally.score_p1, self._tally.score_p2)
            return GameOverState()

        return self

    def _print_players_hand_selections(
        self, selected_hand_p1: str, selected_hand_p2: str
    ):
        self._ui.write(
            "You chose {0}, your opponent chose {1}.\n".format(
                selected_hand_p1, selected_hand_p2
            )
        )

    def _print_players_scores(self):
        self._ui.write(
            "You have {0} points, your opponent has {1}.\n".format(
                self._tally.score_p1, self._tally.score_p2
            )
        )

    def _print_game_result(self, p1: int, p2: int):
        self._ui.write("Game completed!\n")
        if p1 > p2:
            self._ui.write("You win!")
        elif p1 < p2:
            self._ui.write("You lose!")
        else:
            self._ui.write("It's a draw!")
