import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog, QWidget, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.uic.properties import QtGui

from widgets.main_widget import Ui_MainWindow
from widgets.start_dialog import Ui_Dialog

from get_image_by_cords_as_png import get_image_by_cords_as_png


class StartDialog(QDialog, Ui_Dialog):
    def _init__(self):
        super().__init__()
        self.setupUi(self)


class Map(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cords = [0, 0]
        self.zoom = 4
        self.delta = 0.002

        self.cords[0] = float(input())
        self.cords[1] = float(input())
        self.zoom = float(input())
        self.show_map()

        # self.startdialog = StartDialog()
        # self.startdialog.show()
        # self.startdialog.OkBtn.clicked.connect(lambda: self.change_coords_and_size([self.startdialog.xSpinBox.value(),
        #                                     self.startdialog.ySpinBox.value()], self.startdialog.scaleSpinBox.value()))

    def change_coords_and_size(self, cords: list, zoom: float):
        self.cords = cords
        self.zoom = zoom
        self.show_map()
    def show_map(self):
        get_image_by_cords_as_png(cords=tuple(self.cords), zoom=self.zoom, path="temp/a.png")
        pixmap = QPixmap("temp/a.png")
        self.label.setPixmap(pixmap)

    def on_PageUp(self):
        self.zoom += self.delta
        self.show_map()

    def on_PageDown(self):
        self.zoom += self.delta
        self.show_map()

    def on_key_up(self):
        self.cords[1] += self.zoom
        self.show_map()

    def on_key_down(self):
        self.cords[1] -= self.zoom
        self.show_map()

    def on_key_left(self):
        self.cords[0] -= self.zoom
        self.show_map()

    def on_key_right(self):
        self.cords[0] += self.zoom
        self.show_map()

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_PageUp:
            self.on_PageUp()
        elif event.key() == Qt.Key_PageDown:
            self.on_PageDown()
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
