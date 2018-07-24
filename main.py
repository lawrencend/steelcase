"""
	Written by: Nathan Lawrence
	On: 7/21/2018
	Email: ndl0005@uah.edu

	This module creates necessary objects and launches the GUI.
"""

import sys
from PyQt5 import QtWidgets
from src.main_window import MainWindow

# Only run if module is called directly
if __name__ == "__main__":

	# QApplication instance
	app = QtWidgets.QApplication(sys.argv)

	# Start_steelcase instance
	steelcase = MainWindow()

	# Show steelcase gui
	steelcase.show_main_window()

	# Run application and return status to sys	
	sys.exit(app.exec_())