from game.state import State
from game.ui.console_ui import ConsoleUI
from rockpaperscissors.tally import Tally
from game.utils import get_player_hand, get_opponents_hand
from game.current_game_state import PresentResultState


class StartOfGameState(State):
    def __init__(self):
        self.tally = Tally(3)

    def run(self, ui: ConsoleUI) -> State:
        ui.clear_screen()
        ui.write("Starting game...\n")
        self.tally.update(
            get_player_hand(ui),
            get_opponents_hand(),
        )
        return PresentResultState(self.tally)
