import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog, QWidget, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.uic.properties import QtGui

from widgets.main_widget import Ui_MainWindow
from widgets.start_dialog import Ui_Dialog

from get_image_by_cords_as_png import get_image_by_cords_as_png
from get_cords_by_adress import get_cords_by_adress


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
        self.delta_zoom = 1
        self.delta_spn = 1
        self.map_types = ["map", "sat", "sat,skl"]
        self.marks = []
        self.find_address("екатеринбург")
        self.cur_type = 1
        self.size = [450, 450]
        # self.cords[0] = float(input())
        # self.cords[1] = float(input())
        self.zoom = int(input())
        self.spn = self.zoom
        self.show_map()

        # self.startdialog = StartDialog()
        # self.startdialog.show()
        # self.startdialog.OkBtn.clicked.connect(lambda: self.change_coords_and_size([self.startdialog.xSpinBox.value(),
        #                                     self.startdialog.ySpinBox.value()], self.startdialog.scaleSpinBox.value()))

    def change_coords_and_size(self, cords: list, zoom: float):
        self.cords = cords
        self.zoom = zoom
        self.show_map()

    def change_type(self):
        self.cur_type += 1
        self.cur_type = self.cur_type % len(self.map_types)

    def show_map(self):
        if self.zoom < 0:
            self.zoom = 1
        if self.zoom > 17:
            self.zoom = 17
        if self.spn < 0.002:
            self.spn = 0.002
        if self.spn > 100:
            self.spn = 100
        if self.cords[0] > 180:
            self.cords[0] = 180
        if self.cords[0] < -180:
            self.cords[0] = -180
        if self.cords[0] > 90:
            self.cords[0] = 90
        if self.cords[0] < -90:
            self.cords[0] = -90
        print(self.cords, self.zoom, self.map_types[self.cur_type])
        image_path = get_image_by_cords_as_png(tuple(self.cords), tuple(self.size), self.map_types[self.cur_type], self.marks, "temp/a.png", spn=self.spn)
        pixmap = QPixmap(image_path)
        print(pixmap.height())
        self.label.setPixmap(pixmap)

    def find_address(self, address):
        if address != "":
            cords = get_cords_by_adress(address)
            self.set_cords(cords)
            self.marks.clear()
            self.marks.append(f"{','.join(map(str, cords))},pmwtm1")

    def set_cords(self, cords : tuple):
        self.cords = list(cords)

    def on_PageUp(self):
        self.zoom -= self.delta_zoom
        self.spn -= self.delta_spn
        self.show_map()

    def on_PageDown(self):
        self.zoom += self.delta_zoom
        self.spn += self.delta_spn
        self.show_map()

    def on_key_up(self):
        self.cords[1] += self.spn
        self.show_map()

    def on_key_down(self):
        self.cords[1] -= self.spn
        self.show_map()

    def on_key_left(self):
        self.cords[0] -= self.spn
        self.show_map()

    def on_key_right(self):
        self.cords[0] += self.spn
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
