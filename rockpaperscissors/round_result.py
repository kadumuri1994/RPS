from rockpaperscissors.shape import ShapeInterface


class RoundResult:
    def __init__(self, p1: ShapeInterface, p2: ShapeInterface):
        if p1 is None or p2 is None:
            raise TypeError("Shape objects cannot be of None Type.")
        self.score_p1 = 1 if p1.beats(p2) else 0
        self.score_p2 = 1 if p2.beats(p1) else 0
        self.hand_p1 = p1.name()
        self.hand_p2 = p2.name()
