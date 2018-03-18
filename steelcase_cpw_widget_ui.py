# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steelcase_cpw_widget.ui'
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

class Ui_steelcase_cpw_widget(object):
    def setupUi(self, steelcase_cpw_widget):
        steelcase_cpw_widget.setObjectName(_fromUtf8("steelcase_cpw_widget"))
        steelcase_cpw_widget.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(steelcase_cpw_widget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.apply_pw_push_button = QtGui.QPushButton(steelcase_cpw_widget)
        self.apply_pw_push_button.setObjectName(_fromUtf8("apply_pw_push_button"))
        self.horizontalLayout_2.addWidget(self.apply_pw_push_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(steelcase_cpw_widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.pw_line_edit = QtGui.QLineEdit(steelcase_cpw_widget)
        self.pw_line_edit.setText(_fromUtf8(""))
        self.pw_line_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.pw_line_edit.setObjectName(_fromUtf8("pw_line_edit"))
        self.horizontalLayout.addWidget(self.pw_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(steelcase_cpw_widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.cpw_line_edit = QtGui.QLineEdit(steelcase_cpw_widget)
        self.cpw_line_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.cpw_line_edit.setObjectName(_fromUtf8("cpw_line_edit"))
        self.horizontalLayout_3.addWidget(self.cpw_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(steelcase_cpw_widget)
        QtCore.QMetaObject.connectSlotsByName(steelcase_cpw_widget)

    def retranslateUi(self, steelcase_cpw_widget):
        steelcase_cpw_widget.setWindowTitle(_translate("steelcase_cpw_widget", "Change Password", None))
        self.apply_pw_push_button.setText(_translate("steelcase_cpw_widget", "Apply", None))
        self.label.setText(_translate("steelcase_cpw_widget", "Enter New Password:", None))
        self.label_2.setText(_translate("steelcase_cpw_widget", "Confirm New Password:", None))

