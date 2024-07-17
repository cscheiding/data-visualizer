from PyQt6.QtWidgets import QApplication
from frontend.main_window import MainWindow
# from backend.program import Program
import sys


class Session:
    def __init__(self) -> None:
        self.frontend = MainWindow()
        # self.backend = Program()

    def connect(self) -> None:
        pass


if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    session = Session()
    session.connect()

    sys.exit(app.exec())