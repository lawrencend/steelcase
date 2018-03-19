"""
    Written by: Nathan Lawrence
    On: 3/16/2018
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, Start_steelcase, to setup the GUI
    and manage GUI event handeling.

"""
import sys
from PyQt4 import QtCore, QtGui
from pathlib import Path
from steelcase_main_window_ui import Ui_steelcase_main_window
from steelcase_pw_dialog import Pw_dialog
from steelcase_cpw_dialog import Cpw_dialog
from steelcase_cpfc_dialog import Cpfc_dialog
from steelcase_cop_dialog import Cop_dialog
from steelcase_worker import Worker
from steelcase_data_management import Data_management

class Main_window(QtGui.QMainWindow):
    """ Start_steelcase class. This class is used to setup the GUI/
        manage GUI event handeling. Start_steelcase inherites from
        QtGui.Qdialog.
    """

    def __init__(self):
        """ Start_steelcase init method. """

        # init parent classes
        super(Main_window, self).__init__()

        #Ui instance
        self.ui = Ui_steelcase_main_window()

        # Setup ui
        self.ui.setupUi(self)

        # Set initial status to blank
        self.update_status("")

        # Connect the push button to the button        
        QtCore.QObject.connect(self.ui.start_push_button,
                               QtCore.SIGNAL("clicked()"),
                               self.button_clicked)

 #       QtCore.QObject.connect(self.ui.action_enter_calibration_mode,
 #                              QtCore.SIGNAL("triggered()"),
 #                              self.start_pw)

        QtCore.QObject.connect(self.ui.action_change_pass_fail_force_criteria,
                               QtCore.SIGNAL("triggered()"),
                               self.start_cpfc)           

        QtCore.QObject.connect(self.ui.action_change_Password,
                               QtCore.SIGNAL("triggered()"),
                               self.start_cpw)

        QtCore.QObject.connect(self.ui.action_change_output_path,
                               QtCore.SIGNAL("triggered()"),
                               self.start_cop)

        # QThread instance
        self.thread = QtCore.QThread()

        # Pw_dialog instance
        self.ui_pw = Pw_dialog()

        # Cpfc_dialog instance
        self.ui_cpfc_dialog = Cpfc_dialog()

        # Update the cpfc line edit in the main dialog
        self.ui.current_pfc_line_edit.setText(self.ui_cpfc_dialog.current_pfc)

        # Delete self.ui_cpfc_dialog
        self.delete(self.ui_cpfc_dialog)

        # Data_management instance
        self.data_man = Data_management()

    def button_clicked(self):
        """ button clicked slot. Used to determine wether or
            not a thread is currently running and start/stop
            a thread as appropriate.
        """

        # See if self.thread is currently running
        if self.thread.isRunning():

            # Stop it
            self.stop_thread()
            self.update_status("test_stopped")

        # Else start a new thread
        else:

            # Start thread
            self.start_thread()

    def start_thread(self):
        """ start_thread method. Used to create a new QThread instance,
            new Worker instance, connect signals/slots, and start the thread.
        """

        # Worker instance
        self.worker = Worker()

        # QThread instance
        self.thread = QtCore.QThread()

        # Move worker to thread
        self.worker.moveToThread(self.thread)

        # Connect self.thread started() signal to self.update_status
        QtCore.QObject.connect(self.thread,
                               QtCore.SIGNAL("started()"),
                               lambda: self.update_status("running"))

        # Connect self.thread started() signal to self.update_button
        QtCore.QObject.connect(self.thread,
                               QtCore.SIGNAL("started()"),
                               lambda: self.update_button("stop"))

        # Connect self.thread started() signal to self.worker.run
        QtCore.QObject.connect(self.thread,
                               QtCore.SIGNAL("started()"),
                               self.worker.run)

        # Connect self.thread finished() signal to self.update_button
        QtCore.QObject.connect(self.thread,
                               QtCore.SIGNAL("finished()"),
                               lambda: self.update_button("start"))

        # Connect self.worker finished() signal to self.stop_thread
        QtCore.QObject.connect(self.worker,
                               QtCore.SIGNAL("finished()"),
                               self.stop_thread)

        # Connect self.worker finished() signal to self.stop_thread
        QtCore.QObject.connect(self.worker.load_cell,
                               QtCore.SIGNAL("pass()"),
                               lambda: self.update_status("pass"))

        # Connect self.worker finished() signal to self.update_status
        QtCore.QObject.connect(self.worker.load_cell,
                               QtCore.SIGNAL("fail()"),
                               lambda: self.update_status("fail"))

        # Create a new test
        self.data_man.new_test(self.worker)

        # Update the test_id line edit
        self.ui.test_id_line_edit.setText(self.data_man.test_id)

        # Start the thread
        self.thread.start()

    def stop_thread(self):
        """ Method to quit a thread once the worker has finished. """

        # Quit the thread
        self.thread.quit()

        # Wait for the thread to quit
        self.thread.wait()

        # Complete the test by logging data
        self.data_man.complete_test()

    def update_button(self, status):
        """ Method to update the push button. Requires "status" as
            an input.
        """

        # Create text_options dictionary
        text_options = {}
        text_options.update({"start": "Start New Test"})
        text_options.update({"stop": "Stop Test"})

        # Update the push button text with the current status
        self.ui.start_push_button.setText(text_options[status])

    def update_status(self, status):
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

    def start_cpfc(self):
        """Method to make connections and show the password dialog
            before starting the change pass/fail criteria dialog.
        """

        # Connect ui_pw's password match() signal to self.start_cpfc_dialog
        QtCore.QObject.connect(self.ui_pw,
                               QtCore.SIGNAL("match()"),
                               self.start_cpfc_dialog)

        # Upon ui_pw finished() signal, undo the above connection
        QtCore.QObject.connect(self.ui_pw,
                               QtCore.SIGNAL("finished(int)"),
                               lambda: QtCore.QObject.disconnect(self.ui_pw,
                                                                 QtCore.SIGNAL("match()"),
                                                                 self.start_cpfc_dialog))

        # Show the pw dialog
        self.ui_pw.show()

    def start_cpfc_dialog(self):
        """ Method to start the change pass/fail criteria (cpfc) dialog. """

        # Cpfc_dialog instance
        self.ui_cpfc_dialog = Cpfc_dialog()

        QtCore.QObject.connect(self.ui_cpfc_dialog,
                               QtCore.SIGNAL("finished(int)"),
                               lambda: self.ui.current_pfc_line_edit.setText(self.ui_cpfc_dialog.current_pfc))

        QtCore.QObject.connect(self.ui_cpfc_dialog,
                               QtCore.SIGNAL("finished(int)"),
                               lambda: self.delete(self.ui_cpfc_dialog))

        # Show the cpfc dialog
        self.ui_cpfc_dialog.show()

    def start_cpw(self):
        """ Method to make connections and show the password dialog
            before starting the change password (cpw) dialog.
        """

        # Connect ui_pw's password match() signal to self.start_cpw_dialog
        QtCore.QObject.connect(self.ui_pw,
                               QtCore.SIGNAL("match()"),
                               self.start_cpw_dialog)

        # Upon ui_pw finished() signal, undo the above connection
        QtCore.QObject.connect(self.ui_pw,
                               QtCore.SIGNAL("finished(int)"),
                               lambda: QtCore.QObject.disconnect(self.ui_pw,
                                                                 QtCore.SIGNAL("match()"),
                                                                 self.start_cpw_dialog))

        # Show the pw dialog
        self.ui_pw.show()

    def start_cpw_dialog(self):
        """ Method to start the change password (cpw) dialog. """

        # Cpw_dialog instance
        self.ui_cpw = Cpw_dialog()

        QtCore.QObject.connect(self.ui_cpw,
                               QtCore.SIGNAL("finished(int)"),
                               lambda: self.delete(self.ui_cpw))

        # Show to cpw dialog
        self.ui_cpw.show()

    def start_cop(self):
        """ Method to make connections and show the password dialog
            before starting the change output path (cop) dialog.
        """

        # Connect ui_pw's password match() signal to self.start_cop_dialog
        QtCore.QObject.connect(self.ui_pw,
                               QtCore.SIGNAL("match()"),
                               self.start_cop_dialog)

        # Upon ui_pw finished() signal, undo the above connection
        QtCore.QObject.connect(self.ui_pw,
                               QtCore.SIGNAL("finished(int)"),
                               lambda: QtCore.QObject.disconnect(self.ui_pw,
                                                                 QtCore.SIGNAL("match()"),
                                                                 self.start_cop_dialog))

        # Show the pw dialog
        self.ui_pw.show()


    def start_cop_dialog(self):
        """Method to start the change output path (cop) dialog. """

        # Cop_dialog instance
        self.ui_cop_dialog = Cop_dialog()

        # Connect self.ui_cop_dialog's finished() signal to self.delete
        QtCore.QObject.connect(self.ui_cop_dialog,
                               QtCore.SIGNAL("finished(int)"),
                               lambda: self.delete(self.ui_cop_dialog))

        # Show the cop dialog
        self.ui_cop_dialog.show()

    def configure(self):
        """Method to configure the application upon first run.
            Sets user password and output path.
        """

        # Path to check
        path = Path(".steelcase_configured")

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
            self.ui_cpw_dialog = Cpw_dialog()
    
            # Cop_dialog instance
            self.ui_cop_dialog = Cop_dialog()
    
            # Cpfc_dialog instance
            self.ui_cpfc_dialog_dialog = Cpfc_dialog()


            QtCore.QObject.connect(self.ui_cpw_dialog,
                                   QtCore.SIGNAL("finished(int)"),
                                   self.ui_cop_dialog.show)

            QtCore.QObject.connect(self.ui_cop_dialog,
                                   QtCore.SIGNAL("finished(int)"),
                                   self.ui_cpfc_dialog.show)
 
            QtCore.QObject.connect(self.ui_cop_dialog,
                                   QtCore.SIGNAL("finished(int)"),
                                   self.showMaximized)


            QtCore.QObject.connect(self.ui_cpw_dialog,
                                   QtCore.SIGNAL("finished(int)"),
                                   lambda: self.delete(self.ui_cpw_dialog))

            # Connect self.ui_cop_dialog's finished() signal to self.delete
            QtCore.QObject.connect(self.ui_cop_dialog,
                                   QtCore.SIGNAL("finished(int)"),
                                   lambda: self.delete(self.ui_cop_dialog))

            QtCore.QObject.connect(self.ui_cpfc_dialog,
                                   QtCore.SIGNAL("finished(int)"),
                                   lambda: self.delete(self.ui_cpfc_dialog))



            f = open(".steelcase_configured", "w+")
            f.close()

            self.ui_cpw_dialog.show()

        else:

            self.show()


    def delete(self, obj):
        """ Method to delete an object. """

        # Delete the object
        del obj

    def test(self):
        print("works")

    def myShow(self):

        # Check to see if software has been configured
        self.configure()

        

