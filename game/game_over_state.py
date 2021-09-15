from game.state import StateInterface


class GameOverState(StateInterface):
    """After the game is completed, we will be in this state!"""

    def run(self) -> StateInterface:
        return self
