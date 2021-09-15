from rock_paper_scissors.tally import Tally
from rock_paper_scissors.shapes import Shapes


def assert_tally(
    tally: Tally, score_player1: int, shape_p1: str, score_player2: int, shape_p2: str
):
    assert tally.score_p1 == score_player1
    assert tally.score_p2 == score_player2
    assert tally.hand_p1.name() == shape_p1
    assert tally.hand_p2.name() == shape_p2


def test_game():
    """Player who wins maximum rounds wins the game"""
    tally = Tally(5)
    rock = Shapes.rock()
    paper = Shapes.paper()
    scissors = Shapes.scissors()

    tally.hand_p1 = rock
    tally.hand_p2 = paper
    tally.update()
    assert_tally(tally, 0, rock.name(), 1, paper.name())
    assert tally.remaining_nr_of_rounds == 4

    tally.hand_p1 = scissors
    tally.hand_p2 = paper
    tally.update()
    assert_tally(tally, 1, scissors.name(), 1, paper.name())
    assert tally.remaining_nr_of_rounds == 3

    tally.hand_p1 = rock
    tally.hand_p2 = scissors
    tally.update()
    assert_tally(tally, 2, rock.name(), 1, scissors.name())
    assert tally.remaining_nr_of_rounds == 2

    tally.hand_p1 = rock
    tally.hand_p2 = rock
    tally.update()
    assert_tally(tally, 2, rock.name(), 1, rock.name())
    assert tally.remaining_nr_of_rounds == 1

    tally.hand_p1 = rock
    tally.hand_p2 = scissors
    tally.update()
    assert_tally(tally, 3, rock.name(), 1, scissors.name())
    assert tally.remaining_nr_of_rounds == 0


def test_game_is_extended_if_draw():
    """If both the players have equal points after all rounds, another round is played as extension"""
    tally = Tally(1)
    rock = Shapes.rock()
    paper = Shapes.paper()
    scissors = Shapes.scissors()

    tally.hand_p1 = rock
    tally.hand_p2 = rock
    tally.update()
    assert_tally(tally, 0, rock.name(), 0, rock.name())
    assert tally.remaining_nr_of_rounds == 1

    tally.hand_p1 = paper
    tally.hand_p2 = scissors
    tally.update()
    assert_tally(tally, 0, paper.name(), 1, scissors.name())
    assert tally.remaining_nr_of_rounds == 0


def test_game_is_finished_if_one_player_wins_most_rounds():
    """If any of players wins most rounds the game ends without playing any remaining rounds"""
    tally = Tally(3)
    rock = Shapes.rock()
    paper = Shapes.paper()
    scissors = Shapes.scissors()

    tally.hand_p1 = rock
    tally.hand_p2 = scissors
    tally.update()
    assert_tally(tally, 1, rock.name(), 0, scissors.name())
    assert tally.remaining_nr_of_rounds == 2

    tally.hand_p1 = scissors
    tally.hand_p2 = paper
    tally.update()
    assert_tally(tally, 2, scissors.name(), 0, paper.name())
    assert tally.remaining_nr_of_rounds == 0
