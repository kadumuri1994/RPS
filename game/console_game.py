from game.ui.console_ui import ConsoleUI
from game.game_active_state import GameActiveState
from game.game_over_state import GameOverState


class ConsoleGame:
    """This class is used to instantiate console game object used to interact with active and completed game state"""

    def __init__(
        self,
        console_ui: ConsoleUI,
    ):
        if console_ui is None:
            raise TypeError("Console UI object cannot be of None type")
        self.ui = console_ui
        self.ui.clear_screen()
        self.ui.write("Starting game...\n")
        self.state = GameActiveState(self.ui)

    def is_running(self) -> bool:
        self.state = self.state.run(self.ui)
        return not isinstance(self.state, GameOverState)
