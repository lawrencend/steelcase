
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from pathlib import Path

from src.main_window_ui import Ui_MainWindow
from src.cpfc_dialog import CpfcDialog
from src.cop_dialog import CopDialog
from src.cpw_dialog import CpwDialog
from src.pw_dialog import PwDialog

import time
class MainWindow(QtWidgets.QMainWindow):
    """ MainWindow class. This class is used to setup the GUI/
        manage GUI event handeling. MainWindow inherites from
        QtWidgets.QMainWindow.
    """
    def __init__(self):
        """ MainWindow __init__ method. """

        # Parent init
        super().__init__()

        # Ui instance
        self._ui = Ui_MainWindow()
        
        # Pass self to ui to setup
        self._ui.setupUi(self)

        self._cpfc_dialog = CpfcDialog()
        #self._cpfc_dialog.show()

        self._cop_dialog = CopDialog()
        #self._cop_dialog.show()

        self._cpw_dialog = CpwDialog()
        self._cpw_dialog.show()

        self._pw_dialog = PwDialog()
        self._pw_dialog.show()

        # Connections
        self._ui.start_push_button.clicked.connect(self._start_button_clicked)
        self._ui.action_change_pass_fail_force_criteria.triggered.connect(self._start_cpfc)
        self._ui.action_change_password.triggered.connect(self._start_cpw)
        self._ui.action_change_output_path.triggered.connect(self._start_cop)

        # QThread instance
        self._thread = QtCore.QThread()

        # Set initial status
        self._update_status('')

        # Update the cpfc line edit in the main dialog
        self._ui.current_pfc_line_edit.setText(self._cpfc_dialog.current_pfc)

        # Delete self._cpfc_dialog
        self._delete_cpfc()

    @pyqtSlot()
    def _start_button_clicked(self):
        """ button clicked slot. Used to determine wether or
            not a thread is currently running and start/stop
            a thread as appropriate.
        """ 
        pass

    def _update_status(self, status):
        """Method to update the status displayed on the dialog.
            Requires running/pass/fail status as a input.
        """

        # Create text options dictionary
        text_options = {}
        text_options.update({"running": "Running Test..."})
        text_options.update({"pass": "PASSED"})
        text_options.update({"fail": "FAILED"})
        text_options.update({"test_stopped": "Test stopped prematurely..."})
        text_options.update({"":""})

        # Create background colors dictionary
        bc_options = {}
        bc_options.update({"running": "background-color: rgb(255, 255, 255);"})
        bc_options.update({"pass": "background-color: rgb(0, 255, 0);"})
        bc_options.update({"fail": "background-color: rgb(255, 0, 0);"})
        bc_options.update({"test_stopped": "background-color: rgb(255, 85, 0);"})
        bc_options.update({"": "background-color: rgb(255, 255, 255);"})

        # Update the line edit text
        self.ui.status_line_edit.setText(text_options[status])

        # Update the line edit background color
        self.ui.status_line_edit.setStyleSheet(bc_options[status])


    def show_main_window(self):
        """Method to configure the application upon first run.
            Sets user password and output path.
        """

        # Path to check
        path = Path(".configured")

        # See if file exists
        if not path.is_file():

            # Message box success notification
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setWindowTitle("Hi There!")
            msg.setText("Glad to have you as a first time user...")
            msg.setInformativeText("We need you to set your password and output path before using the application.")
            msg.exec_()

            # Cpw_dialog instance
            self._cpw_dialog = CpwDialog()
    
            # Cop_dialog instance
            self._cop_dialog = CopDialog()
    
            # Cpfc_dialog instance
            self._cpfc_dialog = CpfcDialog()


            self._cpw_dialog.finished.connect(self._cop_dialog.show)
    
 
            # QtCore.QObject.connect(self.ui_cop_dialog,
            #                        QtCore.SIGNAL("finished(int)"),
            #                        self.ui_cpfc_dialog.show)
 
            # QtCore.QObject.connect(self.ui_cpfc_dialog,
            #                        QtCore.SIGNAL("finished(int)"),
            #                        self.showMaximized)

            # QtCore.QObject.connect(self.ui_cpw_dialog,
            #                        QtCore.SIGNAL("finished(int)"),
            #                        self.delete_cpw)

            # QtCore.QObject.connect(self.ui_cop_dialog,
            #                        QtCore.SIGNAL("finished(int)"),
            #                        self.delete_cop)

            # QtCore.QObject.connect(self.ui_cpfc_dialog,
            #                        QtCore.SIGNAL("finished(int)"),
            #                        self.delete_cpfc)

            f = open(".steelcase_configured", "w+")
            f.close()

            self.ui_cpw_dialog.show()

        else:

            self.show()

 
     def _delete_cpfc(self):

        del self._cpfc_dialog

    def _delete_cpw(self):

        del self._cpw_dialog

    def _delete_cop(self):

        del self._cop_dialog