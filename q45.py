#Copy a array

import numpy as np
arr = np.array([1,2,3,4,5,6])
arr1=arr.copy()
arr[2] = 42
print(arr1)
print(arr)