"""
	Written by: Nathan Lawrence
	On: 3/17/2018
	Email: Nathan@LawrenceAerospace.com

	This module provides a class, Data_management, to manage all
	data associated with each test and create a unique test id.
"""

import time
import re
import os
from pathlib import Path

class Data_management(object):
	"""Data_management provides methods to manage all
		data associated with each test and create a unique test id.
	"""

	def __init__(self):
		""" Data_management init method. """

		# init parent classes
		super(Data_management, self).__init__()

		# Header string for the output file
		self.header_string = "Test ID,Test Pass/Fail Force [lbf], Pass/Fail Criteria [lbf],Test Result\n"

		# Create names
		self.create_names()

		# Create directories if the don't exist
		self.create_directories()

		# Check to see if there are previous tests on this day
		self.check_for_previous_tests()

	def new_test(self, worker):
		""" Method to be called everytime a new test
			is completed.
		"""
		# Get test id
		self.create_test_id()
		self.create_names()
		self.create_directories()

		# Reference to worker class
		self.worker = worker

	def complete_test(self):
		""" Method called upon the completion of a test.
			Gets needed values, creates an output string,
			and writes the data.
		"""

		# Current pass/fail criteria
		current_pfc = str(self.worker.load_cell.current_pfc)

		# Test status of the completed test
		test_status = self.worker.load_cell.status

		# Force upon test termination
		force = str(self.worker.load_cell.force)

		# Output string to write
		self.out_string = self.test_id + "," + force + "," + current_pfc + "," + test_status + "\n"

		# Write the output string
		self.write_data()

	def create_test_id(self):
		""" Method to create a unique test id
			based on time/date/test number.
		"""

		# Get the current time/date
		c_time = time.strftime('%X %x')

		# Split the time/date into list
		time_list = re.split(' |:|/', c_time)

		# Join the list using underscores
		test_id = "_".join(time_list)

		# Add the test number to the list
		self.test_id = test_id + "_Test_" + str(self.test_num)

		# Increment the test number
		self.test_num += 1

	def create_names(self):
		""" Method to create directory and file names/paths. """

		# Get the data
		date = time.strftime("%x")

		# Split on /
		date = re.split("/", date)

		# Rejoin with _
		date = "_".join(date) 

		# Add .csv to date for the file name
		file_name = date + ".csv"

		# Directory path
		self.dir_path = "~/Desktop/test_data/" + date

		# File path
		self.file_path = self.dir_path + "/" + file_name

	def write_data(self):
		""" Method to write create/append a file with test_data. """

		# Create names and directories incase the date has changed
		self.create_names()
		self.create_directories()

		# Path to check
		path = Path(self.file_path)

		# If file doesn't exist
		if not path.is_file():

			# Open file
			with open(self.file_path, "w") as file:

				# Write the header
				file.write(self.header_string)

				# Write the output string
				file.write(self.out_string)

		# If file does exist
		else:

			# Open file
			with open(self.file_path, "a+") as file:

				# Append the output string
				file.write(self.out_string)

	def create_directories(self):
		"""Method to create directories if they don't exist. """

		# If path doesn't exist
		if not os.path.exists(self.dir_path):

			# Make the directory
			os.makedirs(self.dir_path)

	def check_for_previous_tests(self):
		""" Method to check for previous test data and
			update self.test_num to account for previous tests.
		"""

		# Path to check
		path = Path(self.file_path)

		# See if file exists
		if path.is_file():

			# Open the file and find the most recent test_id
			with open(self.file_path, "r") as file:

				# Read all lines in file
				lines = file.readlines()

				# Get the last line
				last_line = lines[-1]

				# Split and get the test number
				test_id = re.split(",",last_line)[0]
				test_id = re.split("_", test_id)

				# Set self.test_num to the most recent test_num + 1
				self.test_num = int(test_id[-1]) + 1

		# If no file exists
		else:

			# Set test_num = 1
			self.test_num = 1