"""
    Written by: Nathan Lawrence
    On: 3/17/2018
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, Cop_dialog, to change the output path.
"""

from PyQt4 import QtGui, QtCore
import os
from steelcase_cop_dialog_ui import Ui_steelcase_cop_dialog

class Cop_dialog(QtGui.QDialog):
    """This class provides methods to change the output path. """

    def __init__(self):
        """Cop_dialog init method. """

        # Init parent classes
        super(Cop_dialog, self).__init__()

        # Ui instance
        self.ui = Ui_steelcase_cop_dialog()

        # Setup ui
        self.ui.setupUi(self)

        # Open .steelcase_path
        with open(".steelcase_path", "w+") as file:

            # Read the current path
            self.current_path = file.read()

        self.ui.current_path_line_edit.setText(self.current_path)

        # Center
        self.move(QtGui.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

    def accept(self):
        """Accept method. Called upon the ok button being clicked.
            Checks the user input path to see if it is valid.
            If the path is valid, it is saved as the new output path.
        """

        # Get the path from output_path_line_edit
        path = self.ui.output_path_line_edit.text()

        # Check to see if path exists
        if os.path.exists(path):

            # Open .steelcase_path
            with open(".steelcase_path", "w") as file:

                # Write the new path
                file.write(path)

            # Message box error notification
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setWindowTitle("Output Path Changed!")
            msg.setText("Output path changed to:")
            msg.setInformativeText(path)
            msg.exec_()

            # Close the dialog
            self.close()

        # If path doesn't exist, notify user
        else:

            # Message box error notification
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setWindowTitle("Error!")
            msg.setText("Not a valid path!")
            msg.setInformativeText("Please enter a valid directory path.")
            msg.exec_()
