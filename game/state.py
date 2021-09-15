from abc import ABC, abstractmethod


class StateInterface(ABC):
    """This is an abstract class which signifies the game state"""

    @abstractmethod
    def run(self):
        pass

    def _print_players_hand_selections(
        self, selected_hand_p1: str, selected_hand_p2: str
    ):
        pass

    def _print_players_scores(self):
        pass

    def _print_game_result(self, p1: int, p2: int):
        pass
