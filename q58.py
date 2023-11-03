#Creating DataFrame

import pandas as pd
data={
    'calories': [420, 380, 120],
     'duration': [30, 20, 10]
}
newdata = pd.DataFrame(data,index=["Day1","Day2","Day3"])
print(newdata)
print(newdata.loc["Day2"])