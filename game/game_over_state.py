from game.state import State
from game.ui.console_ui import ConsoleUI


class GameOverState(State):
    """After the game is terminated, we will be in this state!"""

    def run(self, _ui: ConsoleUI) -> State:
        return self
