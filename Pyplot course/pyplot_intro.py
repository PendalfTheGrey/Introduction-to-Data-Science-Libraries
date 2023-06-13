from matplotlib import pyplot as plt
import random

#create a arrays
x = [i for i in range(1,101)]
y_1 = []
y_2= []
for i in range (100):
    y_1.append(random.randint(1,101))
    y_2.append(random.randint(1,101))
#add colour and the shape
plt.plot(x,y_1,'gx',x,y_2,'bo')
plt.title('My Linear Graph')
plt.xlabel('Amount of years')
plt.ylabel('Amount of people')
plt.show()

#subplot
plt.subplot(2,1,1)
plt.title('My Subplot graph 1')
plt.plot(x,y_1,'r')
plt.subplot(2,1,2)
plt.title('My Subplot graph 2')
plt.plot(x,y_2,'b')
plt.suptitle('Graphs')
plt.show()

#dots
# plt.scatter(x,y_1)
# plt.show()

#different way of plotting
# lines = plt.plot(x,y_1)
# plt.setp(lines, linewidth=5, color='g')
# plt.show()


