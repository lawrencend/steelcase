from PyQt4 import QtCore, QtGui
from steelcase_cpfc_dialog_ui import Ui_steelcase_cpfc_dialog

class Cpfc_dialog(QtGui.QDialog):

    def __init__(self, parent=None):
        """ Start_steelcase init method. """

        # init parent classes
        super(Cpfc_dialog, self).__init__()

        #Ui instance
        self.ui = Ui_steelcase_cpfc_dialog()

        # Setup ui
        self.ui.setupUi(self)

        with open(".steelcase_pfc", "a+") as file:

            self.current_pfc = file.read()

        self.ui.current_pfc_line_edit.setText(self.current_pfc)

        # Flag window to stay on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def accept(self):

        self.current_pfc = self.check_input(self.ui.new_pfc_line_edit)


        if self.input_status:

            with open(".steelcase_pfc", "w") as file:

                file.write(self.current_pfc)
                
            self.ui.current_pfc_line_edit.setText(self.current_pfc)

            # Message box success notification
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setWindowTitle("Success!")
            msg.setText("Pass/Fail criteria successfully changed to " + self.current_pfc + " [lbf]")
            msg.exec_()

            # Close the cpfc_widget
            self.close()

    def check_input(self, obj):
        """Method to create input for the zero condition. """

        # See if the input can be converted to a float
        try:
            text = obj.text()
            num = float(text)
            self.input_status = True
            return str(num)

        # Except an ValueError and display a message box
        except (ValueError):

            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)

            if text == "":
                msg.setWindowTitle("Input Required!")
                msg.setText("Fill out all the required inputs..")
                msg.setInformativeText("")
                msg.setDetailedText(str(obj))

            else:          
                msg.setWindowTitle("ValueError!")
                msg.setText("'" + text + "' is not a valid input")
                msg.setInformativeText("Entry must be a number.")
                msg.setDetailedText(str(obj))            
            
            # Show the message box
            msg.exec_()

            # Set input_status to false
            self.input_status = False