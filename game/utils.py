import random
from rockpaperscissors.shape import ShapeInterface
from rockpaperscissors.shapes import Shapes
from game.ui.console_ui import ConsoleUI


def get_player_hand(ui: ConsoleUI) -> ShapeInterface:
    player_hand = let_user_select_shape(ui)
    return player_hand


def let_user_select_shape(ui: ConsoleUI) -> ShapeInterface:
    message = "[R]ock, [P]aper or [S]cissors? "
    user_input = ui.read_line(message)
    if not user_input.isalpha() or user_input not in ["r", "p", "s", "R", "P", "S"]:
        raise ValueError(
            "Invalid input type. Please select from [R]ock, [P]aper or [S]cissors."
        )
    user_input = user_input.lower()
    return map_table()[user_input]


def map_table() -> dict:
    return {"r": Shapes.rock(), "p": Shapes.paper(), "s": Shapes.scissors()}


def get_opponents_hand():
    comp_choice = random.choice(["r", "p", "s"])
    return map_table()[comp_choice]
