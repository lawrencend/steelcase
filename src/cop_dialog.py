"""
    Written by: Nathan Lawrence
    On: 3/17/2018
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, Cop_dialog, to change the output path.
"""

import os
from PyQt5.QtWidgets import QDialog, QDesktopWidget, QMessageBox
from src.cop_dialog_ui import Ui_CopDialog


class CopDialog(QDialog):
    """This class provides methods to change the output path. """

    def __init__(self):
        """Cop_dialog init method. """

        # Init parent classes
        super().__init__()

        # Ui instance
        self._ui = Ui_CopDialog()

        # Setup ui
        self._ui.setupUi(self)

        # Open .steelcase_path
        with open(".steelcase_path", "w+") as file:

            # Read the current path
            self.current_path = file.read()

        # Update line edit
        self._ui.current_path_line_edit.setText(self.current_path)

        # Center
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

    def accept(self):
        """Accept method. Called upon the ok button being clicked.
            Checks the user input path to see if it is valid.
            If the path is valid, it is saved as the new output path.
        """

        # Get the path from output_path_line_edit
        path = self._ui.output_path_line_edit.text()

        # Check to see if path exists
        if os.path.exists(path):

            # Open .steelcase_path
            with open(".steelcase_path", "w") as file:

                # Write the new path
                file.write(path)

            # Message box error notification
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Output Path Changed!")
            msg.setText("Output path changed to:")
            msg.setInformativeText(path)
            msg.exec_()

            # Close the dialog
            self.close()

        # If path doesn't exist, notify user
        else:

            # Message box error notification
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error!")
            msg.setText("Not a valid path!")
            msg.setInformativeText("Please enter a valid directory path.")
            msg.exec_()
