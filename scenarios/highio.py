'''
Created on 01-Aug-2016

@author: AdityaN
'''

import scenario 
import sys 
import pickle
import time 

class HighIOWriter(scenario.ScenarioThread):
    
    def __init__(self,testFilePath="test_file.dat",bytesPerWrite=4096):
        super(HighIOWriter,self).__init__() 
        self._bytesPerWrite =   bytesPerWrite 
        self._testFilePath = testFilePath
        
    
    def getWritePayload(self):
        integerSize = sys.getsizeof(0) 
        numberOfAllocations = int(self._bytesPerWrite/integerSize) 
        return range(0,numberOfAllocations) 
    
    def writeToFile(self,payload):
        with open(self._testFilePath,"w+") as binfile:
            pickle.dump(payload,binfile)
        
    def run(self):
        while not self._terminationEvent.isSet():
            payload = self.getWritePayload()
            self.writeToFile(payload)

#TODO : Research Reader 


if __name__ == '__main__':
    o = HighIOWriter("test.txt",32000) 
    o.start()
    time.sleep(20)
    o.terminate()
    