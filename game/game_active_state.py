from game.state import State
from game.ui.console_ui import ConsoleUI
from rock_paper_scissors.tally import Tally
from game.utils import get_player_hand, get_opponents_hand
from game.game_over_state import GameOverState


class GameActiveState(State):
    """Instantiated when game is started and the game would be in this state till all rounds are completed"""

    def __init__(self, ui: ConsoleUI):
        self.ui = ui
        self.tally = Tally(3)

    def run(self, ui: ConsoleUI) -> State:
        self.tally.hand_p1 = get_player_hand(ui)
        self.tally.hand_p2 = get_opponents_hand()

        self.print_players_hand_selections(
            self.tally.hand_p1.name(), self.tally.hand_p2.name()
        )

        self.tally.update()
        self.print_players_scores()

        if self.tally.remaining_nr_of_rounds() == 0:
            self.print_game_result(self.tally.score_p1, self.tally.score_p2)
            return GameOverState()

        return self

    def print_players_hand_selections(
        self, selected_hand_p1: str, selected_hand_p2: str
    ):
        self.ui.write(
            "You chose {0}, your opponent chose {1}.\n".format(
                selected_hand_p1, selected_hand_p2
            )
        )

    def print_players_scores(self):
        self.ui.write(
            "You have {0} points, your opponent has {1}.\n".format(
                self.tally.score_p1, self.tally.score_p2
            )
        )

    def print_game_result(self, p1: int, p2: int):
        self.ui.write("Game completed!\n")
        if p1 > p2:
            self.ui.write("You win!")
        elif p1 < p2:
            self.ui.write("You loose!")
        else:
            self.ui.write("It's a draw!")
        self.ui.write("\n")
