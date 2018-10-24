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

hx.setReferenceUnit(21)
hx.OFFSET = 0


hx.reset()
#hx.tare()

i = 1000
readings = []

while len(readings) <= i:

    try:
        val = hx.getValue()
        #time.sleep(2)
        readings.append(val)
        print("{0: 4.4f}".format(val))
	
	
    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        
read = pd.DataFrame(readings)        
read.to_csv(r'readings.csv')
sys.exit()