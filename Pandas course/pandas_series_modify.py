import numpy as np
import pandas as pd

series = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
print(series)

# Adding
series['g'] = 7 # modifies
print(series)

new_series = pd.concat([series,pd.Series({'h':8,'i':9})]) # returns a new
print(new_series)

# Removing
del series['a'] # modify original
print(series)

dropped_series = series.drop(['e','g']) #return new
print(dropped_series)

value_popped = series.pop('b')
print(series)

# Modify elements
series[0] = 0
print(series)
series['f'] = 60
print(series)

series[:2] = 10 #modify a slice
series[0:3] = [11,12,13]
print(series)

# Renaming
series = series.rename('Series 1')
series = series.rename(str.upper) # Rename the keys
# series = series.reindex(['C', 'A', 'D'])
print(series)


