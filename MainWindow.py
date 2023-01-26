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

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_PageUp:
            print("pup")
        elif event.key() == Qt.Key_PageDown:
            print("pdown")
        elif event.key() == Qt.Key_Up:
            print("up")
        elif event.key() == Qt.Key_Down:
            print("down")
        elif event.key() == Qt.Key_Left:
            print("left")
        elif event.key() == Qt.Key_Right:
            print("riht")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec())
