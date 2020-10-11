# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 08:35:29 2020

@author: saipr
"""

import math
import numpy as np
import matplotlib.pyplot as plt

#---------------------------Inputs--------------------------------------------#

#given points to build an interpolation from:
x1 = np.array([0, np.pi/6, np.pi/4])
y1 = np.array([0, 1/2, 2**.5/2])

#to build an interpolation for - can be one or an array of values
xvals = np.linspace(0, (2*np.pi), 100) #[0, math.pi/6, math.pi/4] 

#optional: The true values, or closer to the true values, of the given values
yexact = np.array([np.sin(x) for x in xvals])


#---------------------------Method--------------------------------------------#

def v_lagrange(xval = xvals, xdat = x1, ydat = y1):
    p = 0.0
    for k in range(0, len(xdat)):
        xk = xdat[k]
        l = 1.0
        for i in range(0, len(xdat)):
            xi = xdat[i]
            if(i != k):
                l = l * ((xval - xi) / (xk - xi))
        p = p + ydat[k] * l
    return p

#---------------------------Testing-------------------------------------------#

#returns a plot of the given estimations
yvals1 = np.array([v_lagrange(x, x1, y1) for x in xvals])
try:
    plt.plot(xvals, yexact, color = 'blue', label = 'Numpy Values')
except: pass
plt.plot(xvals, yvals1, color = 'red', label='LaGrange Values')
plt.xlabel('X Values') 
plt.ylabel('Y Values')
plt.title('Lagrange Interpolation')
plt.legend()
plt.grid()
plt.show()