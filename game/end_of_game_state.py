from game.state import State
from rockpaperscissors.tally import Tally
from game.ui.console_ui import ConsoleUI
from game.game_over_state import ConsoleGameState


class EndOfGameState(State):
    def __init__(self, tally: Tally):
        self.tally = tally

    def run(self, ui: ConsoleUI) -> State:
        ui.write(EndOfGameState.message(self.tally))
        return ConsoleGameState()

    @staticmethod
    def message(tally: Tally) -> str:
        return "{0}\n\nEnd of game!\n".format(
            EndOfGameState.result_message(tally.score_p1, tally.score_p2)
        )

    @staticmethod
    def result_message(p1: int, p2: int) -> str:
        if p1 > p2:
            return "You win!"
        elif p1 < p2:
            return "You loose!"
        return "It's a draw!"
