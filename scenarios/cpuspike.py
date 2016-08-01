'''
Created on 01-Aug-2016

@author: AdityaN
'''
import scenario
import time 
import multiprocessing
class SpikeOneCPU(scenario.ScenarioThread):
    
    def __init__(self):
        super(SpikeOneCPU,self).__init__()
    
    def run(self):
        while not self._terminationEvent.isSet():
            pass 

class CPUSpike(object):
    def __init__(self,numberOfCPUS=0):
        if numberOfCPUS == 0:
            self.numberOfCPUS = multiprocessing.cpu_count()
        else:
            self.numberOfCPUS = numberOfCPUS 
        
        self.threadList = list() 
    
    def beginSpike(self):
        for i in range(0,self.numberOfCPUS):
            t = SpikeOneCPU() 
            t.start() 
            self.threadList.append(t) 
    
    def stopSpike(self):
        for thread in self.threadList:
            thread.terminate() 
        


if __name__ == "__main__":
    
    #===========================================================================
    # o = SpikeOneCPU() 
    # o.start()
    # time.sleep(10)
    # o.terminate()
    #===========================================================================
    # GIL in action may be can't generate more than 30% on a windows system 
    o = CPUSpike(50) 
    o.beginSpike()
    time.sleep(10)
    o.stopSpike()
    