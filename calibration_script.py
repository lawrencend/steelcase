import sys
import time
import pandas as pd
import RPi.GPIO as GPIO
from hx711 import HX711

# choose pins on rpi (BCM5 and BCM6)
hx = HX711(dout=5, pd_sck=6)

# HOW TO CALCULATE THE REFFERENCE UNIT
#########################################
# To set the reference unit to 1.
# Call get_weight before and after putting 1000g weight on your sensor.
# Divide difference with grams (1000g) and use it as refference unit.



hx.setReferenceUnit(1)
hx.reset()
hx.OFFSET = 0
#hx.tare()

print('wait while I zero...')

zero_values = list()
for i in range(1000):

	val = hx.getWeight()
	zero_values.append(val)
	print('current val: ', val, i)

zero_mean = mean(zero_values)
hx.OFFSET = zero_mean

number_of_weights = input('\n\n\nEnter the number of weights to use for calibration:')


reference_calcs = list()
for i in range(number_of_weights):

	weight = input('\n\n\nEnter weight for this test:')


	values = list()
	for i in range(1000):

		val = hx.getWeight()
		values.append(val)
		print('current val: ', val, i)		

	mean = mean(zero_values)

	reference_calcs.append(mean/weight)

print('reference weight is', mean(reference_calcs))	
sys.exit()
