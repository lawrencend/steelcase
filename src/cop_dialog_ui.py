# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/cop_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CopDialog(object):
    def setupUi(self, CopDialog):
        CopDialog.setObjectName("CopDialog")
        CopDialog.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(CopDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(CopDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.output_path_line_edit = QtWidgets.QLineEdit(CopDialog)
        self.output_path_line_edit.setObjectName("output_path_line_edit")
        self.horizontalLayout.addWidget(self.output_path_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(CopDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.current_path_line_edit = QtWidgets.QLineEdit(CopDialog)
        self.current_path_line_edit.setReadOnly(True)
        self.current_path_line_edit.setObjectName("current_path_line_edit")
        self.horizontalLayout_3.addWidget(self.current_path_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(CopDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(CopDialog)
        self.buttonBox.accepted.connect(CopDialog.accept)
        self.buttonBox.rejected.connect(CopDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CopDialog)

    def retranslateUi(self, CopDialog):
        _translate = QtCore.QCoreApplication.translate
        CopDialog.setWindowTitle(_translate("CopDialog", "Dialog"))
        self.label.setText(_translate("CopDialog", "Enter New Output Path:"))
        self.label_2.setText(_translate("CopDialog", "Currnet Output Path:"))

