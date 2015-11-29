'''
Created on Nov 28, 2015

@author: tran
'''
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from lib.AirDataApplication import AirDataApplication 

if __name__ == '__main__':
    app = AirDataApplication("data.txt")
    
    time = raw_input("Enter time: ")
    delta = 0.01
    x_cor = np.arange(32.0, 34.0, delta)
    y_cor = np.arange(-98.0, -96.0, delta)
    
    Z = []
    for i in range(len(y_cor)):
        li = []
        for j in range(len(x_cor)):
            li.append(app.getValueAt(time, x_cor[j], y_cor[i]))
        Z.append(li)
    X,Y = np.meshgrid(x_cor, y_cor)
     
    plt.figure()
    CS = plt.pcolor(X,Y,Z)
    cb=plt.colorbar(CS, orientation = 'horizontal')
    cb.set_label(str(app.airDataCollector.getMetric()))
    plt.title('Contour plot of ' + str(app.airDataCollector.getMetric()) + ' at ' + str(time))
    plt.show()
    