# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/cpfc_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CpfcDialog(object):
    def setupUi(self, CpfcDialog):
        CpfcDialog.setObjectName("CpfcDialog")
        CpfcDialog.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(CpfcDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(CpfcDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.new_pfc_line_edit = QtWidgets.QLineEdit(CpfcDialog)
        self.new_pfc_line_edit.setObjectName("new_pfc_line_edit")
        self.horizontalLayout_2.addWidget(self.new_pfc_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(CpfcDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.current_pfc_line_edit = QtWidgets.QLineEdit(CpfcDialog)
        self.current_pfc_line_edit.setReadOnly(True)
        self.current_pfc_line_edit.setObjectName("current_pfc_line_edit")
        self.horizontalLayout.addWidget(self.current_pfc_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(CpfcDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(CpfcDialog)
        self.buttonBox.accepted.connect(CpfcDialog.accept)
        self.buttonBox.rejected.connect(CpfcDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CpfcDialog)

    def retranslateUi(self, CpfcDialog):
        _translate = QtCore.QCoreApplication.translate
        CpfcDialog.setWindowTitle(_translate("CpfcDialog", "Change Pass/Fail Criteria"))
        self.label_2.setText(_translate("CpfcDialog", "New pass/fail force criteria [lbf]:"))
        self.label.setText(_translate("CpfcDialog", "Current pass/fail force criteria [lbf]:"))

