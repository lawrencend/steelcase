import time
from random import uniform
import pyfirmata


class PyFirmataTeensy:

	def __init__(self):

		self._board = pyfirmata.util.get_the_board(base_dir='/dev/serial/by-id/', identifier='usb-')
		
		# Attributes
		self._servo_max = 180 # mirco-s
		self._servo_min = 0# mirco-s
		self._servo_fully_retracted_pos = 0#2000 # degrees
		self._servo_fully_extended_pos = 135#180 # degrees
		self._servo_current_pos = 135
		self._servo_pos_degrees_to_inches = 4/(self._servo_fully_retracted_pos - self._servo_fully_extended_pos) # inch/degree

		digital_pin = 'd'
		servo_pin_mode =  's' #''p' 
		analog_pin = 'a'
		input_pin_mode = 'i'

		self._servo = self._board.get_pin(str(digital_pin) + ':5:' + str(servo_pin_mode))
		# self._load_cell = self._board.get_pin(f'{analog_pin}:6:{input_pin_mode}')
		#self._board.servo_config(5, self._servo_min, self._servo_max, self._servo_fully_retracted_pos)

		self.iterate = pyfirmata.util.Iterator(self._board)
		self.iterate.start()
		self._servo.write(self._servo_fully_extended_pos)

	# def read_load_cell(self):

	# 	# spring_constant = 2 # lbf/in

	# 	# force = self.get_servo_pos()*spring_constant*uniform(0.97, 1.03)
	# 	# print(self.get_servo_pos())
	# 	# return force
	# 	return self._load_cell.read()

	def get_servo_pos(self):
		print('get servo pos fn :', self._servo_current_pos - self._servo_fully_extended_pos)*self._servo_pos_degrees_to_inches		
		return (self._servo_current_pos - self._servo_fully_extended_pos)*self._servo_pos_degrees_to_inches

	def increment_retract_servo(self):
		print('servo curr pos before : ',self._servo_current_pos) 
		self._servo_current_pos -= 1
		print('servo curr pos after: ',self._servo_current_pos)

		print(self._servo_current_pos, self._servo_fully_retracted_pos)
		if self._servo_current_pos >= self._servo_fully_retracted_pos:
			self._servo.write(self._servo_current_pos)
			print('if because servo>full retract')
			pass 
		else:
			print('else')
			self._servo_current_pos = self._servo_fully_retracted_pos

	def fully_extend_servo(self):

		self._servo_current_pos = self._servo_fully_extended_pos
		#self._servo.write(self._servo_current_pos)
		self._servo.write(self._servo_current_pos)
	def fully_retract_servo(self):

		self._servo_current_pos = self._servo_fully_retracted_pos
		self._servo.write(self._servo_current_pos)

if __name__ == "__main__":

	o = PyFirmataTeensy()
	o.fully_extend_servo()
