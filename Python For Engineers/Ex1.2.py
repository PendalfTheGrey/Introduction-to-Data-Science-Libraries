import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv
# Import data from CSV file
# x_string = []
# y_string = []
# with open('/home/fedor/Desktop/data.csv', 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         x_string.append(row[0])
#         y_string.append(row[1])
# x_string.pop(0)
# y_string.pop(0)
# x_1 = [float(element) for element in x_string]
# y_1 = [float(element) for element in y_string]

#def ols_fit (x, y, transformations : List [ callable ]) : −> List[float ])

data = pd.read_csv('/home/fedor/Desktop/data.csv')

print(data)
# Define the function f(x)

#data = pd.DataFrame({'x':x_1, 'y':y_1})
#print(df)

def f(x, a, b, c):
    return a * x**2 + b * x**5 + c * np.sin(x)

# Extract the x and y values from the data
x = data['x']
y = data['y']
print(type(x))
# Perform curve fitting using the defined function
popt, _ = curve_fit(f, x, y)

# Extract the best-fit parameters
a, b, c = popt

# Plot the data
plt.plot(x, y, 'ro', label='Data')

# Generate x values for the estimated plot
x_estimated = np.linspace(-11, 11, 100)

# Plot the estimated function
plt.plot(x_estimated, f(x_estimated, a, b, c), 'b-', label='Estimate')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
