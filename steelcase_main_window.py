"""
    Written by: Nathan Lawrence
    On: 3/16/2018
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, Start_steelcase, to setup the GUI
    and manage GUI event handeling.

"""
import sys
from PyQt4 import QtCore, QtGui
from steelcase_main_window_ui import Ui_steelcase_main_window
from steelcase_pw_widget import Pw_widget
from steelcase_cpw_widget import Cpw_widget
from steelcase_cpfc_widget import Cpfc_widget
from steelcase_worker import Worker
from steelcase_data_management import Data_management

class Main_window(QtGui.QMainWindow):
    """ Start_steelcase class. This class is used to setup the GUI/
        manage GUI event handeling. Start_steelcase inherites from
        QtGui.QWidget.
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
        # QThread instance
        self.thread = QtCore.QThread()

        # Pw_widget instance
        self.ui_pw = Pw_widget()

        # Cpfc_widget instance
        self.ui_cpfc = Cpfc_widget()

        # Update the cpfc line edit in the main widget
        self.ui.current_pfc_line_edit.setText(self.ui_cpfc.current_pfc)

        # Delete self.ui_cpfc
        self.delete(self.ui_cpfc)

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

        # Connect self.worker finished() signal to self.data_man.complete_test
        QtCore.QObject.connect(self.worker,
                               QtCore.SIGNAL("finished()"),
                               self.data_man.complete_test)

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
        """Method to update the status displayed on the widget.
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
        """Method to make connections and show the password widget
            before starting the change pass/fail criteria widget.
        """

        # Connect ui_pw's password match() signal to self.start_cpfc_widget
        QtCore.QObject.connect(self.ui_pw,
                               QtCore.SIGNAL("match()"),
                               self.start_cpfc_widget)

        # Upon ui_pw close() signal, undo the above connection
        QtCore.QObject.connect(self.ui_pw,
                               QtCore.SIGNAL("close()"),
                               lambda: QtCore.QObject.disconnect(self.ui_pw,
                                                                 QtCore.SIGNAL("match()"),
                                                                 self.start_cpfc_widget))

        # Show the pw widget
        self.ui_pw.show()

    def start_cpfc_widget(self):
        """ Method to start the change pass/fail criteria (cpfc) widget. """

        # Cpfc_widget instance
        self.ui_cpfc = Cpfc_widget()

        QtCore.QObject.connect(self.ui_cpfc,
                               QtCore.SIGNAL("close()"),
                               lambda: self.ui.current_pfc_line_edit.setText(self.ui_cpfc.current_pfc))

        QtCore.QObject.connect(self.ui_cpfc,
                               QtCore.SIGNAL("close()"),
                               lambda: self.delete(self.ui_cpfc))

        # Show the cpfc widget
        self.ui_cpfc.show()

    def start_cpw(self):
        """ Method to make connections and show the password widget
            before starting the change password (cpw) widget.
        """

        # Connect ui_pw's password match() signal to self.start_cpw_widget
        QtCore.QObject.connect(self.ui_pw,
                               QtCore.SIGNAL("match()"),
                               self.start_cpw_widget)

        # Upon ui_pw close() signal, undo the above connection
        QtCore.QObject.connect(self.ui_pw,
                               QtCore.SIGNAL("close()"),
                               lambda: QtCore.QObject.disconnect(self.ui_pw,
                                                                 QtCore.SIGNAL("match()"),
                                                                 self.start_cpw_widget))

        # Show the pw widget
        self.ui_pw.show()

    def start_cpw_widget(self):
        """ Method to start the change password (cpw) widget. """

        # Cpw_widget instance
        self.ui_cpw = Cpw_widget()

        QtCore.QObject.connect(self.ui_cpw,
                               QtCore.SIGNAL("close()"),
                               lambda: self.delete(self.ui_cpw))

        QtCore.QObject.connect(self.ui_cpw,
                               QtCore.SIGNAL("close()"),
                               lambda: self.delete(self.ui_cpw))

        # Show to cpw widget
        self.ui_cpw.show()

    def delete(self, obj):
        """ Method to delete an object. """

        del obj