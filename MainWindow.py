import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QWidget, QApplication

from widgets.main_widget import Ui_MainWindow


class Map(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def show_map(self):
        pass

    def map_left(self):
        pass

    def map_right(self):
        pass

    def map_up(self):
        pass

    def map_down(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec())
