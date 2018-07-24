# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steelcase_pw_dialog.ui'
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

class Ui_steelcase_pw_dialog(object):
    def setupUi(self, steelcase_pw_dialog):
        steelcase_pw_dialog.setObjectName(_fromUtf8("steelcase_pw_dialog"))
        steelcase_pw_dialog.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(steelcase_pw_dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(steelcase_pw_dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.pw_line_edit = QtGui.QLineEdit(steelcase_pw_dialog)
        self.pw_line_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.pw_line_edit.setObjectName(_fromUtf8("pw_line_edit"))
        self.horizontalLayout.addWidget(self.pw_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.pw_status_label = QtGui.QLabel(steelcase_pw_dialog)
        self.pw_status_label.setText(_fromUtf8(""))
        self.pw_status_label.setObjectName(_fromUtf8("pw_status_label"))
        self.gridLayout.addWidget(self.pw_status_label, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(steelcase_pw_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(steelcase_pw_dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), steelcase_pw_dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), steelcase_pw_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(steelcase_pw_dialog)

    def retranslateUi(self, steelcase_pw_dialog):
        steelcase_pw_dialog.setWindowTitle(_translate("steelcase_pw_dialog", "Password Required", None))
        self.label.setText(_translate("steelcase_pw_dialog", "Enter Password:", None))

