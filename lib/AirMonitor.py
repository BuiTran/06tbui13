'''
Created on Nov 24, 2015

@author: tran
'''
import math
class AirMonitor(object):
    '''
    

    '''

    def __init__(self, id, name, lo, la, metric, dataList):
        '''
        Constructor
        '''
        self.id = id
        self.name = name
        self.lo = lo
        self.la = la
        self.metric = metric
        self.dataList = dataList
        
    def getShortname(self):
        return self.name
    
    def getLocation(self):
        return (self.lo, self.la)
    
    def distanceFrom(self,x,y):
        return math.sqrt((self.lo - x)**2 + (self.la - y)**2)
    
    def getData(self):
        return self.dataList
    
    def valueAt(self, t):
        time = t.split(':')
        h = int(time[0])
        m = (time[1])
        minute = float(m[0]) * 10 + float(m[1])
        amount = self.dataList[(h+1) % 23] - self.dataList[h % 23]
        result = self.dataList[h] + (amount * (minute / 60))
        return result
        
        