from game.state import StateInterface
from game.ui.console_ui import ConsoleUI
from rock_paper_scissors.tally import Tally
from game.utils import get_computer_hand
from game.game_over_state import GameOverState


class ComputerVsComputer(StateInterface):
    """Instantiated when game is started in computer vs computer mode and the game would be in this state till all
    rounds are completed"""

    def __init__(self, ui: ConsoleUI):
        self._ui = ui
        self._tally = Tally(3)

    def run(self) -> StateInterface:
        self._ui.write(
            "Current Round: {0}".format(4 - self._tally.remaining_nr_of_rounds)
        )

        self._tally.hand_p1 = get_computer_hand()
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
            "Computer 1 chose {0}, computer 2 chose {1}.\n".format(
                selected_hand_p1, selected_hand_p2
            )
        )

    def _print_players_scores(self):
        self._ui.write(
            "Computer 1 has {0} points, computer 2 has {1}.\n".format(
                self._tally.score_p1, self._tally.score_p2
            )
        )

    def _print_game_result(self, p1: int, p2: int):
        self._ui.write("Game completed!\n")
        if p1 > p2:
            self._ui.write("Computer 1 wins!")
        elif p1 < p2:
            self._ui.write("Computer 2 wins!")
        else:
            self._ui.write("It's a draw!")
        self._ui.write("\n")
