'''
Created on Nov 24, 2015

@author: tran
'''
import math
class AirMonitor(object):
    '''
    Air monitor stations are placed throughout the metroplex in order to measure the concentration of air
    borne pollutants every hour. Each monitor is identified by a unique id (long integer). For convenience,
    we name each station (for example, ‘tollway’, ‘H1’, 'H2', 'H3', ‘LBJ’, etc). We track the location of each
    station in degrees longitude and latitude (for example, -96.7 and 103.45). Each monitor collects a
    certain kind of data (for example "ozone"). And each monitor maintains a collection of timestamped data
    for the daily data observations (collected hourly). Data values are integers and represent parts per million.
    –1 represents a missing data observation.

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
        h = int(t[0])
        minute = float(t[2:])
        amount = self.dataList[h+1] - self.dataList[h]
        result = self.dataList[h] + (amount * (minute / 60))
        return result
        
        