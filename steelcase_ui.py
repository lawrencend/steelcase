# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steelcase_1.ui'
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

class Ui_steelcase_main_window(object):
    def setupUi(self, steelcase_main_window):
        steelcase_main_window.setObjectName(_fromUtf8("steelcase_main_window"))
        steelcase_main_window.resize(800, 577)
        self.centralwidget = QtGui.QWidget(steelcase_main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.start_push_button = QtGui.QPushButton(self.centralwidget)
        self.start_push_button.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.start_push_button.setFont(font)
        self.start_push_button.setObjectName(_fromUtf8("start_push_button"))
        self.gridLayout.addWidget(self.start_push_button, 0, 0, 1, 1)
        self.status_line_edit = QtGui.QLineEdit(self.centralwidget)
        self.status_line_edit.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.status_line_edit.setFont(font)
        self.status_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.status_line_edit.setPlaceholderText(_fromUtf8(""))
        self.status_line_edit.setObjectName(_fromUtf8("status_line_edit"))
        self.gridLayout.addWidget(self.status_line_edit, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        steelcase_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(steelcase_main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        steelcase_main_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(steelcase_main_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        steelcase_main_window.setStatusBar(self.statusbar)

        self.retranslateUi(steelcase_main_window)
        QtCore.QMetaObject.connectSlotsByName(steelcase_main_window)

    def retranslateUi(self, steelcase_main_window):
        steelcase_main_window.setWindowTitle(_translate("steelcase_main_window", "MainWindow", None))
        self.start_push_button.setText(_translate("steelcase_main_window", "START", None))
        self.status_line_edit.setText(_translate("steelcase_main_window", "FAIL", None))

