from PyQt5.QtCore import QObject, pyqtSignal
from numpy import random, mean, std, array
from scipy.stats import linregress
from hx711 import HX711
import time
from datetime import datetime
import pandas as pd

class LoadCell(QObject):
    """This class serves to house readings from the load cell...
        Inherites from QtCore.QObject
    """
    
    hx = HX711(5,6)
    hx.setReferenceUnit(-91557.4896)
    hx.tare()  
    
    def __init__(self):
        """ Load_cell init method """

        # Init parent classes
        super().__init__()

    
        #self..set_reading_format("LSB", "MSB") #monitor if strange readings change first to MSB
        #change this for right reference, converts volatge to force

        self.hx.reset()
        self.hx.tare() 
    
        # Attributes
        self.force = 0
        self._force_readings = list()
        self._time_stamps = list()

        with open('.steelcase_pfc') as file:
            self.current_pfc = float(file.read())

    def update(self,time):
        """ update method to update the load_cell/ associated
            calcs... more later.
        """
        self.raw_load_cell_value = self.hx.getWeight() #self..getWeight(5)
        print('load cell val: ', self.raw_load_cell_value)

        self.hx.powerDown()
        self.hx.powerUp()
#        time.sleep(0.05)
        
        correction= 1#uncomment if give mv#*10**3 #   lb/volt for lbs maybe, but through amplifier what are we getting
        self.force = correction*self.raw_load_cell_value


        self._check_for_failure(time)

        if self.force >= self.current_pfc and self.test_status == 'RUNNING':

            self.continue_test = False
            self.test_status = 'PASSED'

        elif self.test_status == 'FAILED':
            self.continue_test = False

        elif self.test_status == 'RUNNING':
            self.continue_test = True

    def _check_for_failure(self, time):

        if len(self._force_readings) > 0:

            if len(self._force_readings) > 15:

                self._force_readings.pop(0)
                self._force_readings.append(self.force)

                self._time_stamps.pop(0)
                self._time_stamps.append(time)

            slope = linregress(self._force_readings, self._time_stamps)[0]

            if slope < 0:
                self.test_status = 'FAILED'

            elif slope >= 0:
                self.test_status = 'RUNNING'

        else:
            self.test_status = 'RUNNING'

    # def _calibrate_lc(self):




    #     n = 10
    #     i = 0
    #     self.data = []
    #     #self.hx.tare()
       
        
    #     while i <= n:
            
    #         self.datum1 = self.hx.getWeight()
    #         self.datum2 = self.hx.getWeight()
    #         self.datum3 = self.hx.getWeight()
    #         self.datum4 = self.hx.getWeight()
    #         self.datum5 = self.hx.getWeight()
    #         self.datum = (self.datum1+self.datum2+self.datum3+self.datum4+self.datum5)/5 
            
    #         print(self.datum)
    #         self.data.append(self.datum)
    #         i += 1
        
    #     print('length of array ',len(self.data))
    #     self.data_arry = array(self.data)
    #     self.dmean = self.data_arry.mean()
    #     print('Mean : ', self.dmean)
    #     self.dstd = self.data_arry.std()
    #     print('St. Dev : ', self.dstd)
	

if __name__ == '__main__':

    o = LoadCell()
    o._calibrate_lc()
