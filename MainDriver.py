'''
Created on Nov 28, 2015

@author: tran
'''
from lib.AirDataApplication import AirDataApplication 

if __name__ == '__main__':
    app = AirDataApplication("data.txt")
    
    print app.getValueAt("12:15", 5, 6)