#searchsorted

import numpy as np
arr = np.array([1,2,3,4,5,6])
x = np.searchsorted(arr,5)
print(x)