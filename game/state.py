from abc import ABC, abstractmethod
from game.ui.console_ui import ConsoleUI


class State(ABC):
    @abstractmethod
    def run(self, ui: ConsoleUI):
        pass
