#Python program to check whether a specific value is placed at the numpy array or not

import numpy as nm
arr =  nm.array([1,2,3,4,5,6])
value = int(input("Enter the value to search : "))
if value in arr : 
    print("The value is present")
else : 
    print("The value is not found")