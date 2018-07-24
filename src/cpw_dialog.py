"""
    Written by: Nathan Lawrence
    On: 3/16/2018
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, CpwDialog, to manage changing user
    passwords.
"""

from PyQt5.QtWidgets import QDialog, QDesktopWidget, QMessageBox
from argon2 import PasswordHasher
from src.cpw_dialog_ui import Ui_CpwDialog


class CpwDialog(QDialog):
    """This class provides a QDialog and methods to change the
        user password. Derived from QtGui.QDialog.
    """

    def __init__(self):
        """ CpwDialog init method. """

        # init parent classes
        super().__init__()

        #Ui instance
        self._ui = Ui_CpwDialog()

        # Setup ui
        self._ui.setupUi(self)

        # Center
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

    def accept(self):
        """accept method. Method to change user password.
            Checks to ensure passwords match before encrypting
            using argon2's salt and hash.
        """

        # Get the new line password
        pw = self._ui.pw_line_edit.text()

        # Get the confirm line password
        cpw = self._ui.cpw_line_edit.text()

        # Check to see if both passwords match
        if pw == cpw and pw is not '':

            # Hash the password
            ph = PasswordHasher()
            pw_hash = ph.hash(pw)

            # Save the hashed password locally
            with open('.steelcase_pw', 'w') as file:
                file.write(f'{pw_hash}\n')
                file.write(f'{0}\n')
                file.write(f'{False}\n')
                file.write(f'{0}\n')

            # Message box success notification
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Success!')
            msg.setText('Password successfully changed!')
            msg.exec_()

            # Close the CpwDialog
            self.close()

        # If password is blank
        elif pw is '' or cpw is '':

            # Message box error notification
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Error!')
            msg.setText('Please enter your password in both fields!')
            msg.setInformativeText('')
            msg.exec_()

        # If both passwords don't match
        else:

            # Message box error notification
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Error!')
            msg.setText('Passwords do not match!')
            msg.setInformativeText('Please enter the same password in both fields.')
            msg.exec_()
