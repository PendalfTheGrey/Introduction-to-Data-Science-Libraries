import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': {'row1':1,'row2':2,'row3':3}, 'col2': {'row1':4,'row3':5,'row4':6}, 'col3': {'row1':10,'row2':8,'row4':9}})
print(df)
print("--------------------")

# Based on culumns
print(df['col1'])
# print(df.col1) # same thing
print(df.get('col8',default=0)) # safer way
print("--------------------")
# Based on rows
first_row = df.loc['row1']
print(first_row)
print(df.iloc[0]) #if there are no row names
print("--------------------")

# Single Elements
first_1 = df['col1'].loc['row1'] # everything is known
print(first_1)
first_2 = df['col1'].iloc[0] # unknown row label
print(first_2)
first_3 = df.loc['row1','col1']
print(first_3)
first_4 = df.iloc[0,0]
print(first_4)
count = df.count()
print(count)
count_row = df.count(1)
print(count_row)
print(df.min(1))
print(df.min(1))
desc = df.describe()
print(desc)
# Slicing

print("---------------------")
#few max values
print(df.nlargest(2,['col2']))
print(df.nlargest(2,['col3']))
print(df.nsmallest(3,['col1']))
print("---------------------")

#idex of the max
print(df.idxmax(axis=1))
print("---------------------")
idx = df.index
cols = df.columns
print(idx, cols)
print("---------------------")

hist = df.hist(column = ['col1'])

