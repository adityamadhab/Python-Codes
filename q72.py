import matplotlib.pyplot as pit
import numpy as nm
x = nm.array([3,8,1,10])
y = nm.array([4,2,7,3])
pit.subplot(1,2,1) #row, column,position
pit.plot(x,y)

x = nm.array([4,10,9,6])
y = nm.array([7,11,13,17])
pit.subplot(1,2,2)
pit.plot(x,y)
pit.show()