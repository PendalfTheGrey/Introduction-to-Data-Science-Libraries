import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import io

df_1 = pd.DataFrame({'col1': {'row1':1,'row2':2,'row3':3}, 'col2': {'row1':4,'row3':5,'row4':6}})
df_2 = pd.DataFrame({'col1': {'row1':3,'row2':21,'row3':2}, 'col2': {'row1':4,'row2':19,'row4':6}})

print(df_1)
print("------------------------------")

print(df_2)
print("------------------------------")

gt = df_1 > df_2 # element to element
gt = df_1['col1'] > df_2['col2']
gt = df_1.loc['row2'] > df_2.loc['row2']

print(df_1.equals(df_2))
print(gt)
print("------------------------------")

#Iteration
for col in df_1.columns:
    print(col)

print("------------------------------")
for row in df_1.index:
    print(row)
print("------------------------------")
# for col_name, row_value in df_1.items():
#     print(col_name)
#     print(row_value)
#     print("---")

for row_name, col_value in df_1.iterrows():
    print(row_name)
    print(col_value)
    print("---")

data = pd.read_csv('/home/fedor/Desktop/data.csv')
print(data)
data_1 = data.transform(lambda x: x**2)
print(type(data['y']))


# plt.plot(x = data['x'],y = data['y'])
data.plot(x = 'x', y = 'y',kind = 'scatter')
plt.show()



