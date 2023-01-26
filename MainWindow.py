import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog, QWidget, QApplication
from PyQt5.uic.properties import QtGui

from widgets.main_widget import Ui_MainWindow


class Map(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cords = [0,0]
        self.delta = 0.002

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

    def on_key_up(self):
        self.cords[1] += self.delta

    def on_key_down(self):
        self.cords[1] -= self.delta

    def on_key_left(self):
        self.cords[0] -= self.delta

    def on_key_right(self):
        self.cords[0] += self.delta

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_PageUp:
            print("pup")
        elif event.key() == Qt.Key_PageDown:
            print("pdown")
        elif event.key() == Qt.Key_Up:
            self.on_key_up()
        elif event.key() == Qt.Key_Down:
            self.on_key_down()
        elif event.key() == Qt.Key_Left:
            self.on_key_left()
        elif event.key() == Qt.Key_Right:
            self.on_key_right()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec())
