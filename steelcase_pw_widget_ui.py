# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steelcase_pw_widget.ui'
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

class Ui_steelcase_pw_widget(object):
    def setupUi(self, steelcase_pw_widget):
        steelcase_pw_widget.setObjectName(_fromUtf8("steelcase_pw_widget"))
        steelcase_pw_widget.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(steelcase_pw_widget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.submit_pw_push_button = QtGui.QPushButton(steelcase_pw_widget)
        self.submit_pw_push_button.setObjectName(_fromUtf8("submit_pw_push_button"))
        self.horizontalLayout_2.addWidget(self.submit_pw_push_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pw_status_label = QtGui.QLabel(steelcase_pw_widget)
        self.pw_status_label.setText(_fromUtf8(""))
        self.pw_status_label.setObjectName(_fromUtf8("pw_status_label"))
        self.horizontalLayout_3.addWidget(self.pw_status_label)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(steelcase_pw_widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.pw_line_edit = QtGui.QLineEdit(steelcase_pw_widget)
        self.pw_line_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.pw_line_edit.setObjectName(_fromUtf8("pw_line_edit"))
        self.horizontalLayout.addWidget(self.pw_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(steelcase_pw_widget)
        QtCore.QMetaObject.connectSlotsByName(steelcase_pw_widget)

    def retranslateUi(self, steelcase_pw_widget):
        steelcase_pw_widget.setWindowTitle(_translate("steelcase_pw_widget", "Enter Password", None))
        self.submit_pw_push_button.setText(_translate("steelcase_pw_widget", "Submit", None))
        self.label.setText(_translate("steelcase_pw_widget", "Enter Password:", None))

