from rock_paper_scissors.tally import Tally


def test_start_of_game_tally():
    valid_nr_of_total_rounds = [1, 3, 5, 7]
    for total_rounds in valid_nr_of_total_rounds:
        tally = Tally(total_rounds)
        assert tally.score_p1 == 0
        assert tally.score_p2 == 0
        assert tally.remaining_nr_of_rounds == total_rounds
        assert tally.hand_p1 is None
        assert tally.hand_p2 is None
