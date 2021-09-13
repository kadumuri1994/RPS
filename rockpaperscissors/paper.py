from rockpaperscissors.shape import PaperInterface, RockInterface, ShapeInterface


class Paper(PaperInterface):
    def name(self) -> str:
        return "Paper"

    def beats(self, shape: ShapeInterface) -> bool:
        return isinstance(shape, RockInterface)
