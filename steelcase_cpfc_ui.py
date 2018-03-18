# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steelcase_cpfc.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_cpfc_widget(object):
    def setupUi(self, cpfc_widget):
        cpfc_widget.setObjectName(_fromUtf8("cpfc_widget"))
        cpfc_widget.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(cpfc_widget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(cpfc_widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.cpfc_line_edit = QtGui.QLineEdit(cpfc_widget)
        self.cpfc_line_edit.setReadOnly(False)
        self.cpfc_line_edit.setObjectName(_fromUtf8("cpfc_line_edit"))
        self.horizontalLayout.addWidget(self.cpfc_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.apply_push_button = QtGui.QPushButton(cpfc_widget)
        self.apply_push_button.setObjectName(_fromUtf8("apply_push_button"))
        self.horizontalLayout_2.addWidget(self.apply_push_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(cpfc_widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.current_pfc_line_edit = QtGui.QLineEdit(cpfc_widget)
        self.current_pfc_line_edit.setEnabled(False)
        self.current_pfc_line_edit.setObjectName(_fromUtf8("current_pfc_line_edit"))
        self.horizontalLayout_3.addWidget(self.current_pfc_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(cpfc_widget)
        QtCore.QMetaObject.connectSlotsByName(cpfc_widget)

    def retranslateUi(self, cpfc_widget):
        cpfc_widget.setWindowTitle(_translate("cpfc_widget", "Form", None))
        self.label.setText(_translate("cpfc_widget", "Enter new pass/fail force criteria [lbf]:", None))
        self.apply_push_button.setText(_translate("cpfc_widget", "Apply", None))
        self.label_2.setText(_translate("cpfc_widget", "Current pass/fail force criteria [lbf]:", None))

