from game.ui.console_ui import ConsoleUI
from game.start_of_game_state import StartOfGameState
from game.game_over_state import GameOverState


class ConsoleGame:
    def __init__(
        self,
        console_ui: ConsoleUI,
    ):
        if console_ui is None:
            raise TypeError("Console UI object cannot be of None type")
        self.ui = console_ui
        self.game_mode = game_mode
        self.state = StartOfGameState()

    def is_running(self) -> bool:
        self.state = self.state.run(self.ui)
        return not isinstance(self.state, GameOverState)
