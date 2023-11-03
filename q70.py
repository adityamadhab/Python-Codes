import matplotlib.pyplot as pit
import numpy as nm
y = nm.array([4,2,7,3])
font1 = {"family":"serif","color":"blue","size":7}
font2 = {"family":"serif","color":"green","size":7}
font3 = {"family":"serif","color":"red","size":7}
pit.plot(y,'o:r')
pit.xlabel("points",fontdict=font1)
pit.ylabel("value",fontdict=font2)
pit.title("point vs value",fontdict=font3,loc="center")
pit.show()