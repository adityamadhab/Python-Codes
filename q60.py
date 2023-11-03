#Reading a dataset

import pandas as pd
mydata = pd.read_csv("Data.csv")
print(mydata)
print(mydata.head(5))
print(mydata.tail(5))