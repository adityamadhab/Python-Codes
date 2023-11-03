#iloc() : It is a method used to retrieve data from a dataframe which is a position based locator. 
#It takes input as an integer, array of integer, column or function.

#loc() : It takes row or coloumn which is particular labels. It takes input as a single label, list of array and objects with labels

import pandas as pd
mydata = pd.read_csv("Data.csv")
x =  mydata.iloc[:,-1]
print(x)