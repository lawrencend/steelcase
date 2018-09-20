#!/usr/bin/python
#encoding:utf-8

import time

import pyfirmata

# board = pyfirmata.Arduino('/dev/ttyUSB0')  # arduino setup
board = pyfirmata.util.get_the_board(base_dir='/dev/serial/by-id/', identifier='usb-')
iter8 = pyfirmata.util.Iterator(board)
iter8.start()

LED1  = board.get_pin('d:7:o')
LED2 = board.get_pin('d:8:o')
LED3 = board.get_pin('d:9:p')

STEPS = 10000.0

if __name__ == '__main__':

    # increase PWM output in STEPS increments
    for i in range(int(STEPS)):
        

        print(i)
        LED1.write(1)  # hardware-PWM accepts values 0.0 ... 1.0
        LED2.write(0)  # hardware-PWM accepts values 0.0 ... 1.0
        LED3.write(0)
        time.sleep(0.001)
