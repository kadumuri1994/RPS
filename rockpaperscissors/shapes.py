from rockpaperscissors.shape import ShapeInterface
from rockpaperscissors.rock import Rock
from rockpaperscissors.paper import Paper
from rockpaperscissors.scissors import Scissors


class Shapes:
    @staticmethod
    def rock() -> ShapeInterface:
        return Rock()

    @staticmethod
    def paper() -> ShapeInterface:
        return Paper()

    @staticmethod
    def scissors() -> ShapeInterface:
        return Scissors()
