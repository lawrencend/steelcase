# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/cpw_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CpwDialog(object):
    def setupUi(self, CpwDialog):
        CpwDialog.setObjectName("CpwDialog")
        CpwDialog.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(CpwDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(CpwDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pw_line_edit = QtWidgets.QLineEdit(CpwDialog)
        self.pw_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_line_edit.setObjectName("pw_line_edit")
        self.horizontalLayout.addWidget(self.pw_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(CpwDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cpw_line_edit = QtWidgets.QLineEdit(CpwDialog)
        self.cpw_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpw_line_edit.setObjectName("cpw_line_edit")
        self.horizontalLayout_2.addWidget(self.cpw_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(CpwDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(CpwDialog)
        self.buttonBox.accepted.connect(CpwDialog.accept)
        self.buttonBox.rejected.connect(CpwDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CpwDialog)

    def retranslateUi(self, CpwDialog):
        _translate = QtCore.QCoreApplication.translate
        CpwDialog.setWindowTitle(_translate("CpwDialog", "Change Password"))
        self.label.setText(_translate("CpwDialog", "Enter New Password:"))
        self.label_2.setText(_translate("CpwDialog", "Confirm Password: "))

