from rock_paper_scissors.shape import ScissorsInterface, PaperInterface, ShapeInterface


class Scissors(ScissorsInterface):
    def name(self) -> str:
        return "Scissors"

    def beats(self, shape: ShapeInterface) -> bool:
        return isinstance(shape, PaperInterface)
