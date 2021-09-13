from game.console_game import ConsoleGame
from game.ui.console import Console
from game.ui.console_ui import ConsoleUI


def start_program():

    print(
        "Winning Rules of the Rock paper scissor game as follows: \n"
        + "Rock vs Paper -> Paper wins \n"
        + "Rock vs Scissors -> Rock wins \n"
        + "paper vs Scissors -> Scissors wins \n"
    )

    io = Console()
    ui = ConsoleUI(io)

    game = ConsoleGame(ui)
    while game.is_running():
        # Loop until the game is ended
        continue


if __name__ == "__main__":
    start_program()
