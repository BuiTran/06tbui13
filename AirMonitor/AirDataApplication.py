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
        li = [(1 / x.distanceFrom(x,y)) for x in self.airDataCollector.dict.vals()]
        return sum(li)
    
    def getValueAt(self,t,x,y):
        invD = self.getInverseDistance(x, y)
        li = self.airDataCollector.getValueAtFromAll(t)
        
        
        
        
        
        
        
        
        
        
        
        