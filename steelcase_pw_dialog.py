"""
    Written by: Nathan Lawrence
    On: 3/18/2018
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, Pw_dialog, to create !@#
"""

from PyQt4 import QtCore, QtGui
import time
import argon2
from steelcase_pw_dialog_ui import Ui_steelcase_pw_dialog

class Pw_dialog(QtGui.QDialog):

    def __init__(self):
        """ Start_steelcase init method. """

        # init parent classes
        super(Pw_dialog, self).__init__()

        #Ui instance
        self.ui = Ui_steelcase_pw_dialog()

        # Setup ui
        self.ui.setupUi(self)

        self.attempts = 0
        self.lockout_time = 0
        self.locked = False

        self.ph = argon2.PasswordHasher()

    def accept(self):

        with open(".steelcase_pw", "r") as file:

            pw_hash = file.readline()

        pw = self.ui.pw_line_edit.text()

        if self.attempts < 5:

            try:
                if self.ph.verify(pw_hash, pw):

                    QtCore.QObject.emit(self, QtCore.SIGNAL("match()"))
                    self.ui.pw_line_edit.clear()
                    self.attempts = 0.
                    self.ui.pw_status_label.setText("")
                    self.close()

            except argon2.exceptions.VerifyMismatchError:

                self.attempts += 1
                self.ui.pw_status_label.setText("Incorrect Password!")

        else:

            self.lockout_time = time.time()
            self.ui.pw_line_edit.setEnabled(False)
            self.ui.pw_line_edit.setText("Locked! Too many attempts!")
            self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setEnabled(False)
            self.ui.pw_status_label.setText("Account Locked!")
