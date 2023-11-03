#Creating Series

import pandas as pd
a=["apple","mango","orange"]
mydata = pd.Series(a,index=["F1","F2","F3"])
print(mydata)
print(mydata["F2"])