from rockpaperscissors.shape import RockInterface, ScissorsInterface, ShapeInterface


class Rock(RockInterface):
    def name(self) -> str:
        return "Rock"

    def beats(self, shape: ShapeInterface) -> bool:
        return isinstance(shape, ScissorsInterface)
