from game.computer_vs_computer import ComputerVsComputer
from game.player_vs_computer import PlayerVsComputer
from game.ui.console_ui import ConsoleUI


class GameActiveStatePlayerVsComputer(PlayerVsComputer):
    def __init__(self, ui: ConsoleUI):
        super().__init__(ui)

    def run(self):
        return super().run()


class GameActiveStateComputerVsComputer(ComputerVsComputer):
    def __init__(self, ui: ConsoleUI):
        super().__init__(ui)

    def run(self):
        return super().run()
