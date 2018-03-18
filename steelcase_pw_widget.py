from PyQt4 import QtCore, QtGui
import time
import argon2
from steelcase_pw_widget_ui import Ui_steelcase_pw_widget
from steelcase_cpw_widget_ui import Ui_steelcase_cpw_widget

class Pw_widget(QtGui.QWidget):

    def __init__(self, parent = None):
        """ Start_steelcase init method. """

        # init parent classes
        super(Pw_widget, self).__init__()

        #Ui instance
        self.ui = Ui_steelcase_pw_widget()

        # Setup ui
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.submit_pw_push_button,
                               QtCore.SIGNAL("clicked()"),
                               self.check_pw)

        self.attempts = 0
        self.lockout_time = 0
        self.locked = False

        self.ph = argon2.PasswordHasher()

        #self.ui.closeEvent = self.closeEvent

    def check_pw(self):

        with open(".steelcase_pw", "r") as file:

            pw_hash = file.read()

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

            self.ui.pw_line_edit.setEnabled(False)
            self.ui.pw_line_edit.setText("Locked! Too many attempts!")
            self.ui.submit_pw_push_button.setEnabled(False)
            self.ui.pw_status_label.setText("Account Locked!")


    def closeEvent(self, event):
        """Reimplimentation of QWidget's closeEvent method to emit a signal before
            being closed.
        """

        # Emit close() signal
        QtCore.QObject.emit(self, QtCore.SIGNAL("close()"))