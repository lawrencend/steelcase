# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/pw_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PwDialog(object):
    def setupUi(self, PwDialog):
        PwDialog.setObjectName("PwDialog")
        PwDialog.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(PwDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(PwDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pw_line_edit = QtWidgets.QLineEdit(PwDialog)
        self.pw_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_line_edit.setObjectName("pw_line_edit")
        self.horizontalLayout.addWidget(self.pw_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.pw_status_label = QtWidgets.QLabel(PwDialog)
        self.pw_status_label.setText("")
        self.pw_status_label.setObjectName("pw_status_label")
        self.gridLayout.addWidget(self.pw_status_label, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(PwDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(PwDialog)
        self.buttonBox.accepted.connect(PwDialog.accept)
        self.buttonBox.rejected.connect(PwDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PwDialog)

    def retranslateUi(self, PwDialog):
        _translate = QtCore.QCoreApplication.translate
        PwDialog.setWindowTitle(_translate("PwDialog", "Password Required"))
        self.label.setText(_translate("PwDialog", "Enter Password:"))

