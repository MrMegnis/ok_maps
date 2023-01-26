import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QWidget, QApplication
from PyQt5.QtGui import QPixmap

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
        self.coords = [0, 0]
        self.scale = 100

        self.coords[0] = float(input())
        self.coords[1] = float(input())
        self.scale = int(input())
        self.show_map()

        # self.startdialog = StartDialog()
        # self.startdialog.show()
        # self.startdialog.OkBtn.clicked.connect(lambda: self.change_coords_and_size([self.startdialog.xSpinBox.value(),
        #                                     self.startdialog.ySpinBox.value()], self.startdialog.scaleSpinBox.value()))

    def change_coords_and_size(self, coords: list, scale: int):
        self.coords = coords
        self.scale = scale
        self.show_map()

    def show_map(self):
        get_image_by_cords_as_png(tuple(self.coords), size=self.scale, path="temp/a.png")
        pixmap = QPixmap("temp/a.png")
        self.label.setPixmap(pixmap)

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
