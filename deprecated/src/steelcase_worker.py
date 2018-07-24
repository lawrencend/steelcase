"""
    Written by: Nathan Lawrence
    On: 3/16/2016
    Email: Nathan@LawrenceAerospace.com

    This module provides a class, Worker, to manage the execution
    of a test.
"""

from PyQt4 import QtCore, QtGui
from src.steelcase_load_cell import Load_cell

class Worker(QtCore.QObject):
    """ Worker class. Used to create and run all processes
        to complete test. Worker inherites from QtCore.QObject and
        implements pyqtSlots.
    """

    def __init__(self):
        """Worker init method. """

        # init parent classes
        super(Worker, self).__init__()

        # Load_cell instance
        self.load_cell = Load_cell()

    @QtCore.pyqtSlot()
    def run(self):
        """ Run slot. Used to execute processes at a fixed
            freq usin QTimer.
        """

        # QTimer instance
        self.timer = QtCore.QTimer()

        # Connect timer's timeout signal to self.work() slot
        QtCore.QTimer.connect(self.timer, QtCore.SIGNAL("timeout()"),
                              self, QtCore.SLOT("work()"))

        # Connect load_cell's finished() signal to self.stop() slot
        QtCore.QObject.connect(self.load_cell, QtCore.SIGNAL("finished()"),
                               self, QtCore.SLOT("stop()"))

        # Start the timer
        self.timer.start(10)

    @QtCore.pyqtSlot()
    def work(self):
        """ work slot. Used to complete any work needed
            for one iteration of the process.
        """

        # Update load_cell
        self.load_cell.update()

        # More code here for additional processes.

    @QtCore.pyqtSlot()
    def stop(self):
        """ stop slot. Used to emit a finished() signal. """

        # Emit a finished signal.
        QtCore.QObject.emit(self, QtCore.SIGNAL("finished()"))
