#where

import numpy as nm
arr = nm.array([1,2,3,4,5,6])
x = nm.where(arr%2==0)
print(x)