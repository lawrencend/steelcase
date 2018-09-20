"""
    Written by: Nathan Lawrence
    On: 3/16/2016
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, Worker, to manage the execution
    of a test.
"""

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QObject, QTimer, pyqtSlot, pyqtSignal
from src.load_cell import LoadCell

class Worker(QObject):
    """ Worker class. Used to create and run all processes
        to complete test. Worker inherites from QtCore.QObject and
        implements pyqtSlots.
    """

    finished = pyqtSignal(int) 

    def __init__(self):
        """Worker init method. """

        # init parent classes
        super().__init__()

        # Load_cell instance
        self._load_cell = LoadCell()

    @pyqtSlot()
    def run(self):
        """ Run slot. Used to execute processes at a fixed
            freq usin QTimer.
        """

        # QTimer instance
        self._timer = QTimer()

        # # Connect timer's timeout signal to self.work() slot
        self._timer.timeout.connect(self._work)
        # QtCore.QTimer.connect(self.timer, QtCore.SIGNAL("timeout()"),
        #                       self, QtCore.SLOT("work()"))

        # self._timer.finished.connect(self._stop)
        self._load_cell.finished.connect(self._stop)
        # # Connect load_cell's finished() signal to self.stop() slot
        # QtCore.QObject.connect(self.load_cell, QtCore.SIGNAL("finished()"),
        #                        self, QtCore.SLOT("stop()"))

        # Start the timer
        self._timer.start(10)

    @pyqtSlot()
    def _work(self):
        """ work slot. Used to complete any work needed
            for one iteration of the process.
        """
        print(self._timer.remainingTime())
        pass
        # Update load_cell
        self._load_cell.update()

        # More code here for additional processes.

    @pyqtSlot()
    def _stop(self):
        """ stop slot. Used to emit a finished() signal. """

        # Emit a finished signal.
        self.finished.emit(1)
        # QtCore.QObject.emit(self, QtCore.SIGNAL("finished()"))
