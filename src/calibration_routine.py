from src.test_control import TestControl
from src.load_cell import LoadCell

class CalibrationRoutine():

    def __init__(self):

        # Init parent classes
        super().__init__()

        self._test_control = TestControl()
        self._load_cell = LoadCell()

    def _setup(self):
        pass

    def _calibrate(self):
        
        self._cal_data = self._load_cell.get_calibration_data()

    def _write(self):

        with open('.steelcase_cal_data', 'w') as file:

            file.write(self._cal_data)