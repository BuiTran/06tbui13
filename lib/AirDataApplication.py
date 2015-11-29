'''
Created on Nov 25, 2015

@author: tran
'''
from AirDataCollector import AirDataCollector

class AirDataApplication(object):
    '''
    The application 
    '''


    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.airDataCollector = AirDataCollector(fileName)
        
        
    def getInverseDistance(self, x, y):
        li = [(1 / a.distanceFrom(x,y)) for a in self.airDataCollector.dict.values()]
        return sum(li)
    
    def getValueAt(self,t,x,y):
        invD = self.getInverseDistance(x, y)
        liVal = self.airDataCollector.getValueAtFromAll(t)
        liDis = [a.distanceFrom(x,y) for a in self.airDataCollector.dict.values()]
        result = 0
        for i in range(len(liVal)):
            result = result + liVal[0]/liDis[0]/invD
        return result
        
        
        
        
        
        
        
        
        
        
        