#Pandas is a python libary mainly used to analyse the data
#Basic stem: 1. Import pandas libary 2. Creating dataframe 3. Read the data 4. Analyse the data
#Pandas is used for cleaning, exploring, manipulating the dataset based on statistical theory and data size
#In pandas, datasets in multidimensional tables is known as Data Frame(whole table). Series are the colounms of the data set.

import pandas as pd
data={
    'cars': ["BMW", "Volvo", "Ford"],
     'passings': [3, 7, 2]
}
newdata = pd.Series(data)
print(newdata)