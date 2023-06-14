import pandas as pd
import numpy as np

#Comparing
series_1 = pd.Series([1,2,3,4,5,6,np.nan])
series_2 = pd.Series([3,2,1,4,np.nan,6,5])

print(series_1 > series_2)  # 5 is < np.nan
print(series_1.eq(series_2,fill_value = 3))  # 5 is < np.nan
print(series_1[0] < series_2[3])
print(series_1 > 3) # copare to a signal value

#Iterating
is_in = 4 in series_1
print(is_in)

for key,value in series_1.items(): #standart iteration method
    print(key)
    print(value)
for value in series_2:
    print(value)