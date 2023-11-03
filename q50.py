#Flattening = It means convertinng multidimentional arrays to 1D array

import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
new = arr.reshape(-1)
print(new)
