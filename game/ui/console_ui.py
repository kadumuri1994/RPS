from game.ui.console_io import ConsoleIOInterface


class ConsoleUI:
    def __init__(self, console_io: ConsoleIOInterface):
        if console_io is None:
            raise TypeError("Console IO object cannot be of None Type")
        self.io = console_io

    def clear_screen(self):
        self.io.clear_screen()

    def write(self, message: str):
        self.io.write(message)

    def read_line(self, message: str) -> str:
        self.io.write(message)
        return self.io.read_line()
