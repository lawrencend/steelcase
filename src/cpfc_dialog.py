'''
    Written by: Nathan Lawrence
    On: 3/17/2018
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, CpfcDialog, to change the pass/fail criteria.
'''

from PyQt5.QtWidgets import QDialog, QDesktopWidget, QMessageBox
from PyQt5.QtGui import QDoubleValidator
from src.cpfc_dialog_ui import Ui_CpfcDialog


class CpfcDialog(QDialog):
    ''' QDialog class containing methods to change the pass/fail criteria. '''

    def __init__(self):
        ''' Start_steelcase init method. '''

        # init parent classes
        super().__init__()

        #Ui instance
        self._ui = Ui_CpfcDialog()

        # Setup ui
        self._ui.setupUi(self)

        # Validator
        self._ui.new_pfc_line_edit.setValidator(QDoubleValidator())

        with open('.steelcase_pfc', 'a+') as file:

            self._current_pfc = file.read()

        self._ui.current_pfc_line_edit.setText(self._current_pfc)

        # Center
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

    def accept(self):
        ''' Overiding of QDialog accept method. '''

        # Check that input exists
        self._check_input(self._ui.new_pfc_line_edit)
        
        # Get current value
        self._current_pfc = self._ui.new_pfc_line_edit.text()

        if self._input_status:

            with open('.steelcase_pfc', 'w') as file:

                file.write(self._current_pfc)
                
            self._ui.current_pfc_line_edit.setText(self._current_pfc)

            # Message box success notification
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Success!')
            msg.setText(f'Pass/Fail criteria successfully changed to "{self._current_pfc}" [lbf]')
            msg.exec_()

            # Close the cpfc_widget
            self.close()

    def _check_input(self, obj):
        ''' Method to create input for the zero condition. '''

        if obj.text() == '':

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Input Required!')
            msg.setText('Fill out all the required inputs..')
            msg.setInformativeText('')
            msg.setDetailedText(str(obj))         
    
            # Show the message box
            msg.exec_()

            # Set input_status to false
            self._input_status = False

        else:
            self._input_status = True