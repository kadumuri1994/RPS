from rockpaperscissors.round_result import RoundResult
from rockpaperscissors.shape import ShapeInterface


class Tally:
    def __init__(self, rounds: int):
        self.create(Tally.validate_nr_of_rounds(rounds), 0, 0, None, None)

    @classmethod
    def create(
        cls,
        rounds: int,
        p1_score: int,
        p2_score: int,
        p1_hand: str or None,
        p2_hand: str or None,
    ):
        cls.nr_of_rounds = rounds
        cls.score_p1 = p1_score
        cls.score_p2 = p2_score
        cls.hand_p1 = p1_hand
        cls.hand_p2 = p2_hand

    @staticmethod
    def validate_nr_of_rounds(nr: int) -> int:
        if 7 >= nr >= 1 == nr % 2:
            return nr
        raise ValueError()

    def remaining_nr_of_rounds(self) -> int:
        return self.nr_of_rounds

    def update(self, p1: ShapeInterface, p2: ShapeInterface):
        if self.remaining_nr_of_rounds() == 0:
            raise ValueError("All rounds of the game are complete!")
        result = RoundResult(p1, p2)

        score_p1 = self.score_p1 + result.score_p1
        score_p2 = self.score_p2 + result.score_p2

        remaining_nr_of_rounds = Tally.calc_remaining_nr_of_rounds(
            self.remaining_nr_of_rounds(), score_p1, score_p2
        )

        return Tally.create(
            remaining_nr_of_rounds, score_p1, score_p2, result.hand_p1, result.hand_p2
        )

    @staticmethod
    def calc_remaining_nr_of_rounds(nr_of_rounds, score_player1, score_player2):
        rounds = nr_of_rounds - 1

        # If it' a draw and all rounds are played
        if rounds == 0 and score_player1 == score_player2:
            return 1  # Play another round

        # If any of the player has won most rounds
        if (max(score_player1, score_player2) > rounds) and (
            score_player1 != score_player2
        ):
            return 0

        # Keep playing.
        return rounds
