# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/StartDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(302, 148)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OkBtn = QtWidgets.QPushButton(Dialog)
        self.OkBtn.setObjectName("OkBtn")
        self.gridLayout_2.addWidget(self.OkBtn, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.x_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.x_label.setFont(font)
        self.x_label.setObjectName("x_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.x_label)
        self.y_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.y_label.setFont(font)
        self.y_label.setObjectName("y_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.y_label)
        self.scale_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scale_label.setFont(font)
        self.scale_label.setObjectName("scale_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.scale_label)
        self.scaleSpinBox = QtWidgets.QSpinBox(Dialog)
        self.scaleSpinBox.setMinimum(1)
        self.scaleSpinBox.setMaximum(100)
        self.scaleSpinBox.setObjectName("scaleSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.scaleSpinBox)
        self.ySpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.ySpinBox.setMinimum(-90.0)
        self.ySpinBox.setMaximum(90.0)
        self.ySpinBox.setObjectName("ySpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ySpinBox)
        self.xSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.xSpinBox.setMinimum(-180.0)
        self.xSpinBox.setMaximum(180.0)
        self.xSpinBox.setObjectName("xSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.xSpinBox)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.OkBtn.setText(_translate("Dialog", "Ок"))
        self.x_label.setText(_translate("Dialog", "Координата по x"))
        self.y_label.setText(_translate("Dialog", "Координата по y "))
        self.scale_label.setText(_translate("Dialog", "Масштаб"))
