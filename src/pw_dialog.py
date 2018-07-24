"""
    Written by: Nathan Lawrence
    On: 3/18/2018
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, Pw_dialog, to create !@#
"""
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog, QDesktopWidget, QMessageBox, QDialogButtonBox
import time
import argon2
from src.pw_dialog_ui import Ui_PwDialog

class PwDialog(QDialog):
    """ Password dialog class. Contains methods to check passwords and lock if necessary. """
    
    # Password match signal
    pw_match = pyqtSignal()

    def __init__(self):
        """ Start_steelcase init method. """

        # init parent classes
        super().__init__()

        #Ui instance
        self._ui = Ui_PwDialog()

        # Setup ui
        self._ui.setupUi(self)

        # Password hasher
        self._ph = argon2.PasswordHasher()

        # Time to keep password gui locked
        self._lock_time = 5*60  # 5 minutes

        # Number of acceptable attempts
        self.ok_num_attempts = 5

        # Check current status
        self._check_status()

    def _check_status(self):
        """ Method to check the current status, see if the user is locked out. """

        with open(".steelcase_pw", "r") as file:
            self._pw_hash = file.readline().strip('\n')
            self._attempts = float(file.readline().strip('\n'))
            self._locked = self.string_to_bool(file.readline().strip('\n'))
            self._lockout_time = float(file.readline().strip('\n'))   

        if self._locked and time.time() < self._lockout_time + self._lock_time:
            self._lock_gui()

        elif self._locked and time.time() > self._lockout_time + self._lock_time:
            self._unlock_gui()
            self._write_status()

    def _write_status(self):
        """ Method to write out the current status. """

        with open(".steelcase_pw", "w") as file:
            file.write(f'{self._pw_hash}\n')
            file.write(f'{self._attempts}\n')
            file.write(f'{self._locked}\n')
            file.write(f'{self._lockout_time}\n')  

    def accept(self):
        """ Overwritten parent accept method. """

        # Check current status
        self._check_status()

        # Get entered password
        pw = self._ui.pw_line_edit.text()

        if self._attempts < self.ok_num_attempts:

            try:

                # See if password matches hash
                if self._ph.verify(self._pw_hash, pw):

                    # Clear line edit
                    self._ui.pw_line_edit.clear()

                    # Zero out parameters
                    self._unlock_gui()

                    # Emit match signal
                    self.pw_match.emit()
                    
                    # Close gui
                    self.close()

            # Except password mismatch
            except argon2.exceptions.VerifyMismatchError:

                self._attempts += 1
                self._ui.pw_status_label.setText(f"Incorrect Password! {int(self.ok_num_attempts - self._attempts)} attemps left.")
                self._write_status()

        else:

            self._lockout_time = time.time()
            self._lock_gui()
            self._write_status()

    def _lock_gui(self):
        """ Method to lock the gui. """

        self._locked = True
        self._ui.pw_line_edit.setEnabled(False)
        self._ui.pw_line_edit.setText(f'Locked! Too many attempts! ')
        self._ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self._ui.pw_status_label.setText(f'Account Locked! Try again in {int((-time.time() + self._lock_time + self._lockout_time)/60)} minutes')

    def _unlock_gui(self):
        """ Method to unlock the gui. """

        self._locked = False
        self._attempts = 0
        self._lockout_time = 0
        self._ui.pw_line_edit.setEnabled(True)
        self._ui.pw_line_edit.setText("")
        self._ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        self._ui.pw_status_label.setText("")


    def string_to_bool(self, string):
        """ Method to convert a string input to a boolean output. """

        if string == 'True':
            output = True

        elif string == 'False':
            output = False

        else:
            raise ValueError

        return output