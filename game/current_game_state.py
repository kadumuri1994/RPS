from game.end_of_game_state import EndOfGameState
from game.state import State
from rockpaperscissors.tally import Tally
from game.ui.console_ui import ConsoleUI
from game.utils import get_player_hand, get_opponents_hand


class PresentResultState(State):
    def __init__(self, tally: Tally):
        self.tally = tally

    def run(self, ui: ConsoleUI) -> State:
        ui.write(self.message())
        if self.tally.remaining_nr_of_rounds() == 0:
            return EndOfGameState(self.tally)
        self.tally.update(
            get_player_hand(ui),
            get_opponents_hand(),
        )
        return self

    def message(self) -> str:
        return "You chose {0}, your opponent chose {1}.\n".format(
            self.tally.hand_p1, self.tally.hand_p2
        ) + "You have {0} points, your opponent has {1}.\n".format(
            self.tally.score_p1, self.tally.score_p2
        )
