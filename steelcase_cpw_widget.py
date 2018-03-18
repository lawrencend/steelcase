"""
    Written by: Nathan Lawrence
    On: 3/16/2018
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, Cpw_widget, to manage changing user
    passwords.
"""

from PyQt4 import QtCore, QtGui
from argon2 import PasswordHasher
from steelcase_cpw_widget_ui import Ui_steelcase_cpw_widget

class Cpw_widget(QtGui.QWidget):
    """This class provides a QWidget and methods to change the
        user password. Derived from QtGui.QWidget.
    """

    def __init__(self, parent=None):
        """ Cpw_widget init method. """

        # init parent classes
        super(Cpw_widget, self).__init__()

        #Ui instance
        self.ui = Ui_steelcase_cpw_widget()

        # Setup ui
        self.ui.setupUi(self)

        # Connect the apply button to self.change_pw
        QtCore.QObject.connect(self.ui.apply_pw_push_button,
                               QtCore.SIGNAL("clicked()"),
                               self.change_pw)


    def change_pw(self):
        """ change_pw method. Method to change user password.
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

            # Close the cpw_widget
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
