import pandas as pd
import numpy as np

series = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
#print(series)
print(series['a']) #retrive through lable
print(series[0]) #retrive through index
print(series[5]) #last elem
print(series['f']) # last elem
print(series[-1:]) #last elem as a pandas series(slicing)

#retrieving
sixth_elem = series[5] #unsafe return
sixth_elem_safe_1 = series.get(10) #safe return
sixth_elem_safe_2 = series.get('u',default=0) #safer return for data analys
print(sixth_elem_safe_2)


#slicing
last = series[-1:] #last elem as a pandas series(slicing)
first_three = series[0:3]
last_three = series[-3:]
first_two = series[[0,1]]
shuffle = series[[4,3,1,5]]
print(last)
print(first_three)
print(last_three)
print(first_two)
print(shuffle)

#boolean test
gt3 = series[series > 3]
print(gt3)

#to array conversion
indices = series.index
values = series.values
pandas_array = series.array #not really used
print(indices)
print(values)
print(pandas_array)

#properties of series
rnd_series = pd.Series(np.random.rand(10)) #random samples
# print(rnd_series)
rnd_len = rnd_series.count()
rnd_max = rnd_series.max()
rnd_min = rnd_series.min() #many more
print(rnd_len,rnd_max,rnd_min)

description = rnd_series.describe() # gives all the data
print(description)

rnd_sum = series.sum()
print(rnd_sum)

#few largest and smallest
n_largest = rnd_series.nlargest(2)
n_smallest = rnd_series.nsmallest(2)
print(n_largest)
print(n_smallest)

#max id
max_index = rnd_series.idxmax()
min_index = rnd_series.idxmin()
print("------")
print(min_index,max_index)

#value count
histogram = rnd_series.value_counts()
print(histogram)

# same but for other data types
small_series = pd.Series(['a','b','c'])
desc = small_series.describe()

bool_series = pd.Series([True,True,False])
bool_desc = bool_series.describe()
print(bool_desc)

#all true series
all_true = bool_series.all()
any_true = bool_series.any()
print(any_true)
print(all_true)




