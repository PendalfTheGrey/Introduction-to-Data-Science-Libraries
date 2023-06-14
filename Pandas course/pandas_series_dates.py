import pandas as pd
import numpy as np

#Series from Python lists
series = pd.Series([152, 2, 3])
series_1 = pd.Series([True, True, False])
series_2 = pd.Series([152, 2.0, 'Hellob'])
series_3 = pd.Series([152, 2.0, None, np.nan])
series_4 = pd.Series([1, 2, 3], dtype=np.float32)
print(series)

#Series from dict
series_5 = pd.Series({'a': 1,'b': 2,'c': 3,'d': 4})
series_6 = pd.Series({'a': 1.0,'b': 2.0,'c': 3.5,'d': 4.7})
series_7 = pd.Series([1, 2, 3], index=['a','b','c'])
series_8 = pd.Series(10, index= [0,1,2,3,4,5,6]) #same values many times
print(series_8)

#Series from np.arrays
series_9 = pd.Series(np.array([1,2,3,4,5]))
numpy_series = series_9.to_numpy()
print(series_9)
# print(type(series_9))
# print(numpy_series)
# print(type(numpy_series))

#Date Ranges
dates_1 = pd.date_range('20230601',periods=10) #ten days
dates_2 = pd.date_range('20230601',periods=10,freq='M') #ten months
dates_3 = pd.date_range('20230601',periods=10,freq='H') #ten hours
dates_4 = pd.date_range('20230601',periods=10,freq='4H') #every four hours
dates_5 = pd.date_range('20230601','20230602',freq='4H') #start and end date
print(dates_4)

#Ranges and series
dat = pd.date_range('20230602', periods=10)
series_dates = pd.Series([i for i in range(10)], index= dat)
print(series_dates)

#Dates as series
date_as_series = pd.Series(dat)
days = date_as_series.dt.day
print(days)
series_dates_1 = pd.Series([i for i in range(10)], index= date_as_series)
print(series_dates_1)

