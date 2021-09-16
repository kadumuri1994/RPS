from game.game_active_state import (
    GameActiveStatePlayerVsComputer,
    GameActiveStateComputerVsComputer,
)
from game.ui.console_ui import ConsoleUI
from game.game_over_state import GameOverState


class ConsoleGame:
    """This class is used to instantiate console game object"""

    def __init__(
        self,
        console_ui: ConsoleUI,
    ):
        if console_ui is None:
            raise TypeError("Console UI object cannot be of None type")
        self._ui = console_ui
        self._ui.clear_screen()
        self._ui.write("Starting game...\n")

        game_modes_message = (
            "Following are the game modes:\n1.Player vs Computer\n2.Computer vs Computer\n"
            "Enter 1 for Player vs Computer, 2 for Computer vs Computer "
        )
        user_input = self._ui.read_line(game_modes_message)

        while user_input not in ["1", "2"]:
            self._ui.write(
                "Invalid selection. Please enter correct choice from below options:"
            )
            user_input = self._ui.read_line(game_modes_message)

        if user_input == "1":
            self._state = GameActiveStatePlayerVsComputer(self._ui)
        else:
            self._state = GameActiveStateComputerVsComputer(self._ui)

    def is_running(self) -> bool:
        self._state = self._state.run()
        return not isinstance(self._state, GameOverState)
