from abc import ABC, abstractmethod
from game.ui.console_ui import ConsoleUI


class State(ABC):
    """This class signifies the current game state we are in"""

    @abstractmethod
    def run(self, ui: ConsoleUI):
        pass
