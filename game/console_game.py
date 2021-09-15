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
        self._ui.write(
            "Winning Rules of the Rock paper scissor game are as follows: \n"
            + "Rock vs Paper -> Paper wins \n"
            + "Rock vs Scissors -> Rock wins \n"
            + "paper vs Scissors -> Scissors wins \n\n"
            + "Total number of rounds are 3.\n\n"
            + "If a player wins most number of rounds, that player is declared as winner and the game will be "
            + "terminated.\nIf both players get equal points after all rounds, then the game would be extended "
            + "with new round/rounds"
        )

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
