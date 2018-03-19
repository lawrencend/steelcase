"""
    Written by: Nathan Lawrence
    On: 3/16/2018
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, Cpw_dialog, to manage changing user
    passwords.
"""

from PyQt4 import QtCore, QtGui
from argon2 import PasswordHasher
from steelcase_cpw_dialog_ui import Ui_steelcase_cpw_dialog

class Cpw_dialog(QtGui.QDialog):
    """This class provides a QDialog and methods to change the
        user password. Derived from QtGui.QDialog.
    """

    def __init__(self, parent=None):
        """ Cpw_dialog init method. """

        # init parent classes
        super(Cpw_dialog, self).__init__()

        #Ui instance
        self.ui = Ui_steelcase_cpw_dialog()

        # Setup ui
        self.ui.setupUi(self)

        # Flag window to stay on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def accept(self):
        """accept method. Method to change user password.
            Checks to ensure passwords match before encrypting
            using argon2's salt and hash.
        """

        # Get the new line password
        pw = self.ui.pw_line_edit.text()

        # Get the confirm line password
        cpw = self.ui.cpw_line_edit.text()

        # Check to see if both passwords match
        if pw == cpw:

            # Hash the password
            ph = PasswordHasher()
            pw_hash = ph.hash(pw)

            # Save the hashed password locally
            with open(".steelcase_pw", "w") as file:

                file.write(pw_hash)

            # Message box success notification
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setWindowTitle("Success!")
            msg.setText("Password successfully changed!")
            msg.exec_()

            # Close the cpw_dialog
            self.close()

        # If both passwords don't match
        else:

            # Message box error notification
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setWindowTitle("Error!")
            msg.setText("Passwords do not match!")
            msg.setInformativeText("Please enter the same password in both fields.")
            msg.exec_()
