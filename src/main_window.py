
from pathlib import Path
import time
from datetime import datetime


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog, QDesktopWidget, QMessageBox, QDialogButtonBox

from src.main_window_ui import Ui_MainWindow
from src.cpfc_dialog import CpfcDialog
# from src.cop_dialog import cop
from src.cop_dialog import CopDialog
from src.cpw_dialog import CpwDialog
from src.pw_dialog import PwDialog
# from src.worker import Worker
from src.test_control import TestControl
# from src.pyfirmata_teensy import PyFirmataTeensy
from src.data_management import add_test
from src.calibration_routine import CalibrationRoutine

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

        # Connections
        self._ui.start_push_button.clicked.connect(self._start_button_clicked)
        self._ui.action_change_pass_fail_force_criteria.triggered.connect(self._start_cpfc)
        # self._ui.action_enter_calibration_mode.triggered.connect(self._start_calibration_thread)
        # self._ui.action_change_password.triggered.connect(self._start_cpw)
        self._ui.action_change_output_path.triggered.connect(self._start_cop)

        # QThread instance
        self._thread = QtCore.QThread()

        # Set initial status
        self._update_status('')

    def _start_cpfc(self):
        self._cpfc_dialog = CpfcDialog()
        self._cpfc_dialog.finished.connect(lambda: self._ui.current_pfc_line_edit.setText(self._cpfc_dialog.current_pfc))
        self._cpfc_dialog.show()

    def _start_cpw(self):
        self._cpw_dialog = CpwDialog()
        self._cpw_dialog.show()

    def _start_cop(self):
        self._cop_dialog = CopDialog()
        self._cop_dialog.show()

    @pyqtSlot()
    def _start_button_clicked(self):
        """ button clicked slot. Used to determine wether or
            not a thread is currently running and start/stop
            a thread as appropriate.
        """ 
        # self._start_test_thread()
        # See if self.thread is currently running
        if self._thread.isRunning():

            # Stop it
            self._test_control._stop()

            # self._stop_thread()
            # self._update_status("test_stopped")
            # self._update_button("start")

        # Else start a new thread
        else:

            # Start thread
            self._start_test_thread()

    def _start_test_thread(self):
        """ start_thread method. Used to create a new QThread instance,
            new Worker instance, connect signals/slots, and start the thread.
        """




        # self._thread.start()
        self._test_control = TestControl()
        self._thread = QtCore.QThread()
        self._test_control.moveToThread(self._thread)
        self._thread.started.connect(self._test_control.run)

        # Connect self.thread started() signal to self.update_status
        self._update_status("running")
        self._update_button("stop")
        self._test_id = datetime.now()
        self._ui.test_id_line_edit.setText(self._test_id)
        # self._thread.started.connect(lambda: self._update_status("running"))

        # Connect self.thread started() signal to self.update_button
        # self._thread.started.connect(lambda: self._update_button("stop"))

        # Connect self._test_control value_updated() to self._update_status
        self._test_control.value_updated.connect(lambda value: self._update_status("update", value))
        self._test_control.taring_scale.connect(lambda value: self._update_status("taring", value))

        # Connect self._test_control finished() signal to self._stop_test
        self._test_control.finished.connect(lambda test_df: self._stop_test(test_df))

        self._thread.start()

    # def _start_calibration_thread(self):
    #     """ start_thread method. Used to create a new QThread instance,
    #         new Worker instance, connect signals/slots, and start the thread.
    #     """
    #     # self._thread.start()
    #     self._test_control = TestControl()
    #     self._thread = QtCore.QThread()
    #     self._test_control.moveToThread(self._thread)
    #     self._thread.started.connect(self._test_control.run)

    #     # Connect self.thread started() signal to self.update_status
    #     self._thread.started.connect(lambda: self._update_status("running"))

    #     # Connect self.thread started() signal to self.update_button
    #     self._thread.started.connect(lambda: self._update_button("stop"))

    #     # Connect self._test_control finished() signal to self._stop_test
    #     self._test_control.finished.connect(lambda test_df: self._stop_test(test_df))

    #     self._thread.start()


    def _stop_thread(self):

          # Quit the thread
        self._thread.quit()

        # Wait for the thread to quit
        self._thread.wait()      


    @pyqtSlot()
    def _stop_test(self, test_df):
        """ Method to quit a thread once the worker has finished. """

        self._stop_thread()

        test_result = test_df['test_status'].tail(1).values[0]

        if test_result == 'PASSED':
            self._update_status('pass')

        elif test_result == 'FAILED':
            self._update_status('fail')

        elif test_result == 'RUNNING':
            self._update_status('test_stopped')

        self._update_button('start')
        # print(test_df)
        # Complete the test by logging data
        # self.data_man.complete_test()

        add_test(test_df, self._test_id)
    
    def _update_button(self, status):
        """ Method to update the push button. Requires "status" as
            an input.
        """

        # Create text_options dictionary
        text_options = {}
        text_options.update({"start": "Start New Test"})
        text_options.update({"stop": "Stop Test"})

            # Update the push button text with the current status
        self._ui.start_push_button.setText(text_options[status])
  
    def _update_status(self, status, *value):
        """Method to update the status displayed on the dialog.
            Requires running/pass/fail status as a input.
        """

        # print(value)
        # Create text options dictionary
        text_options = {}
        text_options.update({"running": "Running Test..."})

        if value is not None and len(value)>0:
            text_options.update({"update": "Running Test... CFV = " + str(value[0])})
        else:
            text_options.update({"update": "Running Test..."})

        text_options.update({"taring": "Taring Scale, Wait..."})
        text_options.update({"pass": "PASSED"})
        text_options.update({"fail": "FAILED"})
        text_options.update({"test_stopped": "Test stopped prematurely..."})
        text_options.update({"":""})

        # Create background colors dictionary
        bc_options = {}
        bc_options.update({"running": "background-color: rgb(255, 255, 255);"})
        bc_options.update({"update": "background-color: rgb(255, 255, 255);"})
        bc_options.update({"taring": "background-color: rgb(255, 255, 255);"})
        bc_options.update({"pass": "background-color: rgb(0, 255, 0);"})
        bc_options.update({"fail": "background-color: rgb(255, 0, 0);"})
        bc_options.update({"test_stopped": "background-color: rgb(255, 85, 0);"})
        bc_options.update({"": "background-color: rgb(255, 255, 255);"})

        # Update the line edit text
        if status == 'update':
            f = self._ui.status_line_edit.font()
            f.setPointSize(25)
            self._ui.status_line_edit.setFont(f)

        else:
            f = self._ui.status_line_edit.font()
            f.setPointSize(45)
            self._ui.status_line_edit.setFont(f)

        self._ui.status_line_edit.setText(text_options[status])

        # Update the line edit background color
        self._ui.status_line_edit.setStyleSheet(bc_options[status])


    def show_main_window(self):
        """Method to configure the application upon first run.
            Sets user password and output path.
        """

        # Path to check
        path = Path(".configured")

        # See if file exists
        if not path.is_file():

            # Message box success notification
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
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

            # Connect cpw finished to cop show
            self._cpw_dialog.finished.connect(self._cop_dialog.show)

            # Connect cop finished to cpfc show
            self._cop_dialog.finished.connect(self._cpfc_dialog.show)

            # Connect cpfc finished to self.showMaximized
            self._cpfc_dialog.finished.connect(lambda: self._ui.current_pfc_line_edit.setText(self._cpfc_dialog.current_pfc))
            self._cpfc_dialog.finished.connect(self.showMaximized)

            # Write .configured token
            f = open(".configured", "w+")
            f.close()

            # Show the cpw
            self._cpw_dialog.show()

        else:

            with open('.steelcase_pfc') as file:
                current_pfc = file.read()

            # Update the cpfc line edit in the main dialog
            self._ui.current_pfc_line_edit.setText(current_pfc)

            # Show the mainwindow
            self.showMaximized()