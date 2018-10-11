# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:11:21 2018

@author: Krysta
"""

import pandas as pd
import numpy as np
from hx711 import HX711
import time
from datetime import datetime

def listData(self,force):
    self.forces.append(force)
    self.samp_time.append(time.time)
    return self.forces,self.samp_time


class lcReader():
    def __init__(self):
        self.forces = []
        self.samp_time = []
        self.dataDF = pd.DataFrame()

    #get unique test name, should probably print on screen at end of test
    d = datetime.today()
    fname = str(d.year)+str(d.month)+str(d.day)+str(d.hour)+str(d.minute)+str(d.second)    
    
    #initiate load cell
    hx = HX711(5,6)
    hx.set_reading_format("LSB", "MSB") #monitor if strange readings change first to MSB
    #change this for right reference, converts volatge to force
#    hx.set_reference_unit(92)
    hx.reset()
    hx.tare()   
    
    while start_test == True:
        try:
            force_new = hx.get_value(5)
            self.forces.append(force_new)
            self.samp_time.append(time.time)            
            

            #timing need to be coordinated with motion of actuator
            hx.power_down()
            hx.power_up()
            time.sleep(0.5)
    
    
    

    
    
