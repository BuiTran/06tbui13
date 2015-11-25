'''
Created on Nov 24, 2015

@author: tran
'''

class AirDataCollector(object):
    '''
    Our AirDataCollector class allows us to access a specified data monitor from the collection of monitors. An
    AirDataCollector functions like a back-end database managing the monitors.

    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.dict = {}
        