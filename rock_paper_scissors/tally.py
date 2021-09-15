from rock_paper_scissors.round_result import RoundResult
from rock_paper_scissors.shape import ShapeInterface


class Tally:
    """This class includes information like player scores, player hand selections, remaining number of rounds, etc"""

    def __init__(self, rounds: int):
        self.remaining_nr_of_rounds = Tally.validate_nr_of_rounds(rounds)
        self.score_p1 = 0
        self.score_p2 = 0
        self.hand_p1 = None
        self.hand_p2 = None

    @staticmethod
    def validate_nr_of_rounds(nr: int) -> int:
        if 7 >= nr >= 1 == nr % 2:
            return nr
        raise ValueError()

    def update(self):
        if self.remaining_nr_of_rounds == 0:
            raise ValueError("All rounds of the game are complete!")

        result = RoundResult(self.hand_p1, self.hand_p2)

        self.score_p1 = self.score_p1 + result.score_p1
        self.score_p2 = self.score_p2 + result.score_p2

        self.remaining_nr_of_rounds = Tally.calc_remaining_nr_of_rounds(
            self.remaining_nr_of_rounds, self.score_p1, self.score_p2
        )

    @staticmethod
    def calc_remaining_nr_of_rounds(nr_of_rounds, score_player1, score_player2):
        rounds = nr_of_rounds - 1

        # If it' a draw and all rounds are played
        if rounds == 0 and score_player1 == score_player2:
            return 1  # Play another round

        # If any of the player has won most rounds
        if abs(score_player1 - score_player2) > rounds:
            return 0

        # Keep playing.
        return rounds
