"""
    Written by: Nathan Lawrence
    On: 3/16/2016
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, TestControl, to manage the execution
    of a test.
"""

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QObject, QTimer, pyqtSlot, pyqtSignal
from pandas import DataFrame
from datetime import datetime
from src.load_cell import LoadCell
from src.pyfirmata_teensy import PyFirmataTeensy

class TestControl(QObject):
    """ TestControl class. Used to create and run all processes
        to complete test. TestControl inherites from QtCore.QObject and
        implements pyqtSlots.
    """

    _pyfirmata = PyFirmataTeensy()
    finished = pyqtSignal(DataFrame)
    value_updated = pyqtSignal(float)
    taring_scale = pyqtSignal(int)

    def __init__(self):
        """TestControl init method. """

        # init parent classes
        super().__init__()

        self._load_cell = LoadCell()

        self.test_data = DataFrame()

        self.headers = ['datetime', 'time', 'load_cell_force', 'raw_load_cell_value',
                        'servo_command_sent', 'pass_fail_criteria_used', 'test_status']
    
        self.data = list()

        self.data.append(['waiting', 'waiting', 'waiting', 'waiting',
                        'waiting', 'waiting', 'waiting'])

    @pyqtSlot()
    def run(self):
        """ Run slot. Used to execute processes at a fixed
            freq usin QTimer.
        """
        # QTimer instance
        self._timer = QTimer()

        # # Connect timer's timeout signal to self.work() slot
        self._timer.timeout.connect(self._work)

        # self._timer.finished.connect(self._stop)
        # self._load_cell.finished.connect(self._stop)

        self.taring_scale.emit(1)
        self._load_cell.hx.tare()


        # Start the timer
        self._timer.start(50) # / 10 hz. Placeholder value.

    @pyqtSlot()
    def _work(self):
        """ work slot. Used to complete any work needed
            for one iteration of the process.
        """

#        raw_load_cell_value = self._pyfirmata.read_load_cell() #
        current_datetime = datetime.now()
        current_time = current_datetime.timestamp()

        self._load_cell.update(current_time)

        if self._load_cell.continue_test and self._pyfirmata.continue_test:
            self._pyfirmata.increment_retract_servo()
            servo_command_sent = 'increment_retract'
            temp = [current_datetime, current_time, self._load_cell.force, self._load_cell.raw_load_cell_value,
                    servo_command_sent, self._load_cell.current_pfc, self._load_cell.test_status]

            self.data.append(temp)
            # self.value_updated.emit(self._load_cell.force)

        else:
            servo_command_sent = None
            temp = [current_datetime, current_time, self._load_cell.force, self._load_cell.raw_load_cell_value,
                servo_command_sent, self._load_cell.current_pfc, self._load_cell.test_status]

            self.data.append(temp)
            self._stop()


    @pyqtSlot()
    def _stop(self):
        """ stop slot. Used to emit a finished() signal. """

        self._test_data = DataFrame(self.data, columns=self.headers)

        # ensure servo is extended
        self._pyfirmata.fully_extend_servo()

        # Emit a finished signal.
        self.finished.emit(self._test_data)
