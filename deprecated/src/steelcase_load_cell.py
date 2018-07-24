from PyQt4 import QtCore
from numpy import random

class Load_cell(QtCore.QObject):
    """This class serves to house readings from the load cell...
        Inherites from QtCore.QObject
    """

    def __init__(self):
        """ Load_cell init method """

        # Init parent classes
        super(Load_cell, self).__init__()

        # Temp force attr
        self.force = 0
        self.status = "stopped"

        with open(".steelcase_pfc", "r") as file:

            self.current_pfc = float(file.read())
        
    def update(self):
        """ update method to update the load_cell/ associated
            calcs... more later.
        """

        self.force += 1

        print("Force = ", self.force/100)

        # Stop if force is greater than 1000. 
        # In the future, this is where we determine a pass/fail status.

        if self.force >= self.current_pfc*100:

            num = random.randint(0, 2)

            if num == 0:

                self.status = "fail"

            else:

                self.status = "pass"

            # Stop
            self.stop()


    def stop(self):
        """ stop method to emit a finished signal. """

        # Emit a finished signal.
        QtCore.QObject.emit(self, QtCore.SIGNAL("finished()"))

        if self.status == "pass":

            QtCore.QObject.emit(self, QtCore.SIGNAL("pass()"))

        elif self.status == "fail":

            QtCore.QObject.emit(self, QtCore.SIGNAL("fail()"))            