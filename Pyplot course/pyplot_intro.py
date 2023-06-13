from matplotlib import pyplot as plt
import random

#create a arrays
x = [i for i in range(1,101)]
y = []
for i in range (100):
    y.append(random.randint(1,101))
plt.plot(x,y)
plt.show()