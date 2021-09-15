from rock_paper_scissors.shape import PaperInterface, RockInterface, ShapeInterface


class Paper(PaperInterface):
    def name(self) -> str:
        return "Paper"

    def beats(self, shape: ShapeInterface) -> bool:
        return isinstance(shape, RockInterface)
