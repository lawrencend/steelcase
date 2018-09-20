import time
import pyfirmata


class PyFirmataTeensy:

	def __init__(self):

		self._board = pyfirmata.util.get_the_board(base_dir='/dev/serial/by-id/', identifier='usb-')

		self._pin1 = self._board.get_pin('d:7:o')
		self._pin2 = self._board.get_pin('d:8:o')
		self._pin3 = self._board.get_pin('d:9:p')
		self._led  = self._board.get_pin('d:13:o') 

	def run(self):

		iterate = pyfirmata.util.Iterator(self._board)
		iterate.start()

		self._pin1.write(1)
		self._pin2.write(0)
		self._pin3.write(1)
		self._led.write(1)

		for i in range(0, 25):

			time.sleep(1)
			self._led.write(0)
			self._pin3.write(0)

			time.sleep(1)
			self._led.write(1)
			self._pin3.write(1)

		time.sleep(1)
		self._led.write(0)
		self._pin3.write(0)

if __name__ == "__main__":

	o = PyFirmataTeensy()
	o.run()