class ShapeInterface:
    """Implement the below method that implements this interface"""

    def name(self) -> str:
        pass

    def beats(self, _shape) -> bool:
        pass


class RockInterface(ShapeInterface):
    pass


class PaperInterface(ShapeInterface):
    pass


class ScissorsInterface(ShapeInterface):
    pass
