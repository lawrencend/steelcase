# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steelcase_main_window.ui'
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
        steelcase_main_window.resize(884, 651)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(steelcase_main_window.sizePolicy().hasHeightForWidth())
        steelcase_main_window.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(steelcase_main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.current_pfc_line_edit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_pfc_line_edit.sizePolicy().hasHeightForWidth())
        self.current_pfc_line_edit.setSizePolicy(sizePolicy)
        self.current_pfc_line_edit.setReadOnly(True)
        self.current_pfc_line_edit.setObjectName(_fromUtf8("current_pfc_line_edit"))
        self.horizontalLayout.addWidget(self.current_pfc_line_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.start_push_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_push_button.sizePolicy().hasHeightForWidth())
        self.start_push_button.setSizePolicy(sizePolicy)
        self.start_push_button.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.start_push_button.setFont(font)
        self.start_push_button.setObjectName(_fromUtf8("start_push_button"))
        self.gridLayout.addWidget(self.start_push_button, 3, 0, 1, 1)
        self.status_line_edit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_line_edit.sizePolicy().hasHeightForWidth())
        self.status_line_edit.setSizePolicy(sizePolicy)
        self.status_line_edit.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(56)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.status_line_edit.setFont(font)
        self.status_line_edit.setText(_fromUtf8(""))
        self.status_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.status_line_edit.setPlaceholderText(_fromUtf8(""))
        self.status_line_edit.setObjectName(_fromUtf8("status_line_edit"))
        self.gridLayout.addWidget(self.status_line_edit, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.test_id_line_edit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_id_line_edit.sizePolicy().hasHeightForWidth())
        self.test_id_line_edit.setSizePolicy(sizePolicy)
        self.test_id_line_edit.setMinimumSize(QtCore.QSize(340, 0))
        self.test_id_line_edit.setReadOnly(True)
        self.test_id_line_edit.setObjectName(_fromUtf8("test_id_line_edit"))
        self.horizontalLayout_2.addWidget(self.test_id_line_edit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        steelcase_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(steelcase_main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        steelcase_main_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(steelcase_main_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        steelcase_main_window.setStatusBar(self.statusbar)
        self.action_enter_calibration_mode = QtGui.QAction(steelcase_main_window)
        self.action_enter_calibration_mode.setObjectName(_fromUtf8("action_enter_calibration_mode"))
        self.action_change_pass_fail_force_criteria = QtGui.QAction(steelcase_main_window)
        self.action_change_pass_fail_force_criteria.setObjectName(_fromUtf8("action_change_pass_fail_force_criteria"))
        self.action_change_Password = QtGui.QAction(steelcase_main_window)
        self.action_change_Password.setObjectName(_fromUtf8("action_change_Password"))
        self.menuSettings.addAction(self.action_enter_calibration_mode)
        self.menuSettings.addAction(self.action_change_pass_fail_force_criteria)
        self.menuSettings.addAction(self.action_change_Password)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(steelcase_main_window)
        QtCore.QMetaObject.connectSlotsByName(steelcase_main_window)

    def retranslateUi(self, steelcase_main_window):
        steelcase_main_window.setWindowTitle(_translate("steelcase_main_window", "Steelcase NDDTS", None))
        self.label.setText(_translate("steelcase_main_window", "Current Pass/Fail Criteria [lbf]:", None))
        self.start_push_button.setText(_translate("steelcase_main_window", "Start New Test", None))
        self.label_2.setText(_translate("steelcase_main_window", "Test ID:", None))
        self.menuSettings.setTitle(_translate("steelcase_main_window", "Settings", None))
        self.action_enter_calibration_mode.setText(_translate("steelcase_main_window", "Enter calibration mode...", None))
        self.action_change_pass_fail_force_criteria.setText(_translate("steelcase_main_window", "Change Pass/Fail Force Criteria...", None))
        self.action_change_Password.setText(_translate("steelcase_main_window", "Change Password...", None))

