from PyQt5.QtCore import QObject, pyqtSignal
from numpy import random

class LoadCell(QObject):
    """This class serves to house readings from the load cell...
        Inherites from QtCore.QObject
    """

    finished = pyqtSignal(int)
    passed = pyqtSignal(int)
    failed = pyqtSignal(int)

    def __init__(self):
        """ Load_cell init method """

        # Init parent classes
        super().__init__()

        # Temp force attr
        self._force = 0
        self._status = "stopped"

        with open(".steelcase_pfc", "r") as file:

            self._current_pfc = float(file.read())
        
    def update(self):
        """ update method to update the load_cell/ associated
            calcs... more later.
        """

        self._force += 1

        print("Force = ", self._force/100)

        # Stop if force is greater than 1000. 
        # In the future, this is where we determine a pass/fail status.

        if self._force >= self._current_pfc*100:

            num = random.randint(0, 2)

            if num == 0:

                self._status = "fail"

            else:

                self._status = "pass"

            # Stop
            self._stop()


    def _stop(self):
        """ stop method to emit a finished signal. """

        # Emit a finished signal.
        self.finished.emit(1)

        if self._status == "pass":

            self.passed.emit(1)

        elif self._status == "fail":

            self.failed.emit(1)