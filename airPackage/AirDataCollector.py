'''
Created on Nov 24, 2015

@author: tran
'''


from AirMonitor import AirMonitor

import os.path


class AirDataCollector(object):
    '''
    Our AirDataCollector class allows us to access a specified data monitor from the collection of monitors. An
    AirDataCollector functions like a back-end database managing the monitors.

    '''


    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.dict = {}
        self.readFile(fileName)
        
    def readFile(self, fileName):
        f = open(fileName)
        lines = f.read().splitlines()
        for text in lines:
            listWord = text.split()
            id = int(listWord[0])
            name = listWord[1]
            lo = float(listWord[2])
            la = float(listWord[3])
            metric = listWord([4])
            dataList = [int(s) for s in listWord[5:]]
            airMonitor = AirMonitor(id, name, lo, la, metric, dataList)
            self.dict[id] = airMonitor
    
    def getMonitorList(self):
        for x in self.dict:
            print(self.dict[x].name)
    
    def getMonitorById(self,id):
        return self.dict[id]
    
    def getValueAtFromId(self,t,id):
        return self.getMonitorById(id).valueAt(t)
    
    def getValueAtFromAll(self, t):
        return [x.valueAt(t) for x in self.dict.values()]
            
        
        