from PyQt5.QtCore import QObject, pyqtSignal
from numpy import random
from scipy.stats import linregress

class LoadCell(QObject):
    """This class serves to house readings from the load cell...
        Inherites from QtCore.QObject
    """

    def __init__(self):
        """ Load_cell init method """

        # Init parent classes
        super().__init__()

        # Attributes
        self.force = 0
        self._force_readings = list()
        self._time_stamps = list()

        with open('.steelcase_pfc') as file:
            self.current_pfc = float(file.read())

    def update(self, raw_load_cell_value, time):
        """ update method to update the load_cell/ associated
            calcs... more later.
        """


        correction= 1
        self.force = correction*raw_load_cell_value


        self._check_for_failure(time)

        if self.force >= self.current_pfc and self.test_status == 'RUNNING':

            self.continue_test = False
            self.test_status = 'PASSED'

        elif self.test_status == 'FAILED':
            self.continue_test = False

        elif self.test_status == 'RUNNING':
            self.continue_test = True

    def _check_for_failure(self, time):

        if len(self._force_readings) > 0:

            if len(self._force_readings) > 15:

                self._force_readings.pop(0)
                self._force_readings.append(self.force)

                self._time_stamps.pop(0)
                self._time_stamps.append(time)

            slope = linregress(self._force_readings, self._time_stamps)[0]

            if slope < 0:
                self.test_status = 'FAILED'

            elif slope >= 0:
                self.test_status = 'RUNNING'

        else:
            self.test_status = 'RUNNING'