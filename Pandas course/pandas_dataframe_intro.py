import pandas as pd
import numpy as np

df = pd.DataFrame([1,2,3],dtype=np.float16)
df_1 = pd.DataFrame(['1','2','3'])
df_2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
df_3 = pd.DataFrame([[1,2,3,4],[5,6],[7,8,9]]) # will add NaN for empty
df_4 = pd.DataFrame(5, index=[0,1], columns=[0,1,2]) # fill a matrix
df_5 = pd.DataFrame(5, index=['a','b'], columns=['col1','col2','col3']) # fill a matrix

df_6 = pd.DataFrame([1,2,3], index=['a','b','c'])
df_7 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['a','b','c'])
# print(df_7)

# Dictionary
df_dict = pd.DataFrame({'col1':[1,2,3],'col2':[4,5,6]})
df_dict_1 = pd.DataFrame({'col1': pd.Series([1,2,3]), 'col2': pd.Series([1,2,3])})
print(df_dict_1)




