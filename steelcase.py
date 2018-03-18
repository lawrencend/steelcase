"""
	Written by: Nathan Lawrence
	On: 3/16/2018
	Email: Nathan@LawrenceAerospace.com

	This module creates necessary objects and launches GUI.
"""

import sys
from PyQt4 import QtGui
from steelcase_main_window import Main_window

# Only run if module is called directly
if __name__ == "__main__":

	# QApplication instance
	app = QtGui.QApplication(sys.argv)

	# Start_steelcase instance
	steelcase = Main_window()

	# Show steelcase gui
	steelcase.show()

	# Run application and return status to sys	
	sys.exit(app.exec_())