from game.console_game import ConsoleGame
from game.ui.console import Console
from game.ui.console_ui import ConsoleUI


def start_program():
    io = Console()
    ui = ConsoleUI(io)

    game = ConsoleGame(ui)
    while game.is_running():
        # Loop until the game is ended
        continue


if __name__ == "__main__":
    start_program()
