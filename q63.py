#Python program to reverse a numpy array

import numpy as nm
arr = nm.array([1,2,3,4,5,6])
#Using the flip function
arr1 = nm.flip(arr)
#Slicing
arr2 = arr[::-1]
print(arr1)
