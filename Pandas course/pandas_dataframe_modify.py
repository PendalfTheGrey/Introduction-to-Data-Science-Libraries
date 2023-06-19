import pandas as pd
import numpy as np

df_1 = pd.DataFrame({'col1': {'row1':1,'row2':2,'row3':3}, 'col2': {'row1':4,'row3':5,'row4':6}, 'col3': {'row1':10,'row2':8,'row4':9}})
df_2 = pd.DataFrame({'col1': {'row1':3,'row2':21,'row3':2}, 'col2': {'row1':4,'row2':19,'row4':6}, 'col3': {'row1':10,'row2':8,'row2':10}})

print(df_1)
print("--------------------")
print(df_2)

print("--------------------")
#add row
df_1['col4'] = [1,2,3,4]
print(df_1)
df_1.loc['row5'] = [10,3,90,2]
print(df_1)

combined = df_1.combine_first(df_2) #over writes unless it is not a number
combined_1 = pd.concat([df_1,df_2]) # creates double rows
print(combined)
print(combined_1)
print("--------------------")
dropped = df_1.dropna()
print(dropped)
print("--------------------")
droppped_1 = df_1.drop(index=['row4'],columns=['col3'])
print(droppped_1)
print("--------------------")

del df_1['col4']
print(df_1)

#Reassigning
print("--------------------")
df_1['col1'] = [2,3,4,5,6]
df_1['col1'] = pd.Series({'row1':1,'row2':2,'row3':3,'row4':4,'row5':5})
print(df_1)
print("--------------------")
df_1.loc['row1'] = [10,11,12]
df_1.loc['row1'] = pd.Series({'col1':1.0,'col2':2, 'col3':5})
print(df_1)
print("--------------------")
df_1 = df_1.fillna(0)
print(df_1)

#Restructuring
df_1 = df_1.reindex(columns=['col3','col1','col2'])
print(df_1)
print("--------------------")
df_1 = df_1.reindex(columns=['col3','col1','col2','col4'])
df_1 = df_1.fillna(0)
print(df_1)
print("--------------------")
del df_1['col4']
df_1.columns = ['x1','x2','x3']
print(df_1)
print("--------------------")
df_1 = df_1.reindex(index=['row4','row2','row1','row5','row2'])
print(df_1)
print("--------------------")
df_1.index = ['y1','y2','y3','y4','y5']
print(df_1)

