# # import pandas as pd
# # data = pd.read_csv("/home/fedor/Desktop/data.csv")
# # print(data)
# # for row in data:
# #     print(row)
#
# import matplotlib.pyplot as plt
# import csv
#
# x = []
# y = []
#
# with open('/home/fedor/Desktop/data.csv', 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#
#     for row in plots:
#         x.append(row[0])
#         y.append(row[1])
# x.pop(0)
# y.pop(0)
# x_1 = [float(element) for element in x]
# y_1 = [float(element) for element in y]
# print(x_1)
# print(y_1)
# plt.scatter(x_1,y_1)
# plt.show()
#
# def obj(x,a,b):
#     return a * x + b
#
# popt, _ = curve_fit()
#
# # plt.bar(x, y, color='g', width=0.72, label="Age")
# # plt.xlabel('Names')
# # plt.ylabel('Ages')
# # plt.title('Ages of different persons')
# # plt.legend()
# # plt.show()

import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import statsmodels.api as sm
import math
x_string = []
y_string = []
with open('/home/fedor/Desktop/data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x_string.append(row[0])
        y_string.append(row[1])
x_string.pop(0)
y_string.pop(0)
x_1 = [float(element) for element in x_string]
y_1 = [float(element) for element in y_string]
# print(x_1)
# print(y_1)
plt.scatter(x_1,y_1)
plt.show()

df = pd.DataFrame({'x':x_1, 'y':y_1})
#print(df)
y = df['y']
x = df['x']

x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
#print(model.summary())

print(model.params)

#find line of best fit
#a, b ,c= np.polyfit(df['x'], df['y'], 3)
coef = np.polyfit(df['x'], df['y'], 5)
print(coef)
#add points to plot
plt.scatter(df['x'], df['y'], color='purple')

#add line of best fit to plot
#plt.plot(df['x'], a*df['x']+b)
#plt.plot(df['x'], a*df['x']**2 + b*df['x']**5 + c*math.sin(df['x']))
plt.show()

#add fitted regression equation to plot
#plt.text(1, 90, 'y = ' + '{:.3f}'.format(b) + ' + {:.3f}'.format(a) + 'x', size=12)

#add axis labels
plt.xlabel('x')
plt.ylabel('y')
