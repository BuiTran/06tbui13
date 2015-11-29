'''
Created on Nov 28, 2015

@author: tran
'''
from airPackage.AirDataApplication import AirDataApplication

if __name__ == '__main__':
    app = AirDataApplication("data.txt")
    print app.getValueAt(12, 5, 6)