'''
Created on 01-Aug-2016

@author: AdityaN
'''
import scenario
import sys 
import time 

class HighMemory(scenario.ScenarioThread):
    def __init__(self,allocationBytes=4096,totalInitialBytes=( 100*1024*1024)):
        super(HighMemory,self).__init__()
        self._allocationBytes = allocationBytes
        self._totalInitalBytes = totalInitialBytes
        self._allocationList = list()
    
    def getAllocationPayload(self):
        integerSize = sys.getsizeof(0)
        numberOfIntegers = int(self._allocationBytes/integerSize) 
        allocationUnit = range(0,numberOfIntegers) 
        return allocationUnit
    
    def run(self):
          
        initialAllocations = self._totalInitalBytes/self._allocationBytes
        
        for i in range(0,initialAllocations):
            self._allocationList.append(self.getAllocationPayload())
        
        while not self._terminationEvent.isSet():
            self._allocationList.append(self.getAllocationPayload())
             
        

if __name__ == '__main__':
    o = HighMemory()
    o.start() 
    time.sleep(20)
    o.terminate() 