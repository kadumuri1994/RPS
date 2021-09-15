from rock_paper_scissors.shape import ShapeInterface
from rock_paper_scissors.rock import Rock
from rock_paper_scissors.paper import Paper
from rock_paper_scissors.scissors import Scissors


class Shapes:
    """This class contains static methods which returns each of shape objects"""

    @staticmethod
    def rock() -> ShapeInterface:
        return Rock()

    @staticmethod
    def paper() -> ShapeInterface:
        return Paper()

    @staticmethod
    def scissors() -> ShapeInterface:
        return Scissors()
