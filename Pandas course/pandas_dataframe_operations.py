import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': {'row1':1,'row2':2,'row3':3}, 'col2': {'row1':4,'row3':5,'row4':6}, 'col3': {'row1':10,'row2':8,'row4':9}})
print(df)
print("----------------------")

#Arithmetic
df = df + 5 #add 5 to all
print(df)
df = df**2
print(df)
df = df.add(-10,fill_value= 0)
print(df)

#Function
def f(x):
    return 2*x + 5
df = df.apply(f)
print(df)
df = df.transform(np.sqrt)
df = df.fillna(1)
print(df)
print("----------------------")
df = df.transform(lambda x : x**2)
print(df)
df_double = df.transform([np.square,np.log])
print(df_double)
print("----------------------")
df_1 = df.transform({'col1':np.log})
print(df_1)
# df = df.transpose()

#type casting
df = df.astype('int')
df = df.astype(np.float16)
print("----------------------")

#sorting
df_1 = df.sort_index(axis=0,ascending=False)
print(df)
df_1 = df.sort_index(axis=1,ascending=False)
print(df_1)

df = df.sort_values('col3',axis=0,ascending=False)
df = df.sort_values('row2',axis=1,ascending=False)

print(df)








