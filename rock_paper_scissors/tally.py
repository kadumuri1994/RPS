from rock_paper_scissors.round_result import RoundResult
from rock_paper_scissors.shape import ShapeInterface


class Tally:
    """This class includes information like player scores, player hand selections, remaining number of rounds, etc"""

    def __init__(self, rounds: int):
        self.remaining_nr_of_rounds = Tally._validate_nr_of_rounds(rounds)
        self._score_p1 = 0
        self._score_p2 = 0
        self._hand_p1 = None
        self._hand_p2 = None

    @property
    def hand_p1(self):
        return self._hand_p1

    @hand_p1.setter
    def hand_p1(self, value: ShapeInterface):
        self._hand_p1 = value

    @property
    def hand_p2(self):
        return self._hand_p2

    @hand_p2.setter
    def hand_p2(self, value: ShapeInterface):
        self._hand_p2 = value

    @property
    def score_p1(self):
        return self._score_p1

    @score_p1.setter
    def score_p1(self, value: int):
        self._score_p1 = value

    @property
    def score_p2(self):
        return self._score_p2

    @score_p2.setter
    def score_p2(self, value: int):
        self._score_p2 = value

    @staticmethod
    def _validate_nr_of_rounds(nr: int) -> int:
        if 7 >= nr >= 1 == nr % 2:
            return nr
        raise ValueError()

    def update(self):
        if self.remaining_nr_of_rounds == 0:
            raise ValueError("All rounds of the game are complete!")

        result = RoundResult(self.hand_p1, self.hand_p2)

        self.score_p1 = self.score_p1 + result.score_p1
        self.score_p2 = self.score_p2 + result.score_p2

        self.remaining_nr_of_rounds = Tally._calc_remaining_nr_of_rounds(
            self.remaining_nr_of_rounds, self.score_p1, self.score_p2
        )

    @staticmethod
    def _calc_remaining_nr_of_rounds(nr_of_rounds, score_player1, score_player2):
        rounds = nr_of_rounds - 1

        # If it' a draw and all rounds are played
        if rounds == 0 and score_player1 == score_player2:
            return 1  # Play another round

        # If any of the player has won most rounds
        if abs(score_player1 - score_player2) > rounds:
            return 0

        # Keep playing.
        return rounds
