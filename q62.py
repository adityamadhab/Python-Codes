#Python program to build an array combining two different numpy array

import numpy as nm
arr1 = nm.array([1,2,3,4])
arr2 = nm.array([5,6,7,8])
arr3 = nm.concatenate((arr1,arr2))
print(arr3) 