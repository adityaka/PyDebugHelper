'''
Created on 01-Aug-2016

@author: AdityaN
'''

import threading 
import abc 



class ScenarioThread (threading.Thread):
    def __init__(self):
        super(ScenarioThread,self).__init__() 
        self.daemon = True 
        self._terminationEvent = threading.Event() 
    
    @abc.abstractmethod
    def run(self):
        pass
    
    def terminate(self):
        self._terminationEvent.set() 
        
        
     