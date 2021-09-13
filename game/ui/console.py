from os import system, name
from game.ui.console_io import ConsoleIOInterface


class Console(ConsoleIOInterface):
    def clear_screen(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def write(self, msg: str):
        print(msg)

    def read_line(self) -> str:
        return input()
