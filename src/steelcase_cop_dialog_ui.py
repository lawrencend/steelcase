# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steelcase_cop_dialog.ui'
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

class Ui_steelcase_cop_dialog(object):
    def setupUi(self, steelcase_cop_dialog):
        steelcase_cop_dialog.setObjectName(_fromUtf8("steelcase_cop_dialog"))
        steelcase_cop_dialog.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(steelcase_cop_dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(steelcase_cop_dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.output_path_line_edit = QtGui.QLineEdit(steelcase_cop_dialog)
        self.output_path_line_edit.setObjectName(_fromUtf8("output_path_line_edit"))
        self.horizontalLayout.addWidget(self.output_path_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(steelcase_cop_dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.current_path_line_edit = QtGui.QLineEdit(steelcase_cop_dialog)
        self.current_path_line_edit.setReadOnly(True)
        self.current_path_line_edit.setObjectName(_fromUtf8("current_path_line_edit"))
        self.horizontalLayout_3.addWidget(self.current_path_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(steelcase_cop_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(steelcase_cop_dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), steelcase_cop_dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), steelcase_cop_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(steelcase_cop_dialog)

    def retranslateUi(self, steelcase_cop_dialog):
        steelcase_cop_dialog.setWindowTitle(_translate("steelcase_cop_dialog", "Dialog", None))
        self.label.setText(_translate("steelcase_cop_dialog", "Enter New Output Path:", None))
        self.label_2.setText(_translate("steelcase_cop_dialog", "Currnet Output Path:", None))

