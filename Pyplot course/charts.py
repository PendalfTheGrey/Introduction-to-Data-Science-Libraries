from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import random
x = [i for i in range (1,101)]
y_1 = []
y_2 = []
for i in range(1,101):
    y_1.append(random.randint(1,101))
    y_2.append(random.randint(1,101))

# Use dict for Bar Charts instead of lists since it is more convenient
bar_chart_data = {'Cats':25,'Dogs':13, 'Rats':8}
pet_plot = plt.bar(bar_chart_data.keys(),bar_chart_data.values())
plt.title('Pets in German Households')
plt.xlabel('Pets')
plt.ylabel('Amount')
plt.setp(pet_plot, color = 'r')
plt.show()

# Piecharts
# Dict is also used for these charts
#this was unnecessary since pieplot does it automatically
sum_of_pets = sum(bar_chart_data.values())
pie_chart_data_compex = {'Cats':(bar_chart_data['Cats']/sum_of_pets),'Dogs':(bar_chart_data['Dogs']/sum_of_pets), 'Rats':(bar_chart_data['Rats']/sum_of_pets)}

pie_chart_data = bar_chart_data
explode = (0,0.1,0.1)
plt.pie(pie_chart_data.values(), labels=pie_chart_data.keys(), startangle=90, explode=explode,shadow=True)
plt.show()

#Histograms
histogram_dataset = []
for i in range(30):
    histogram_dataset.append(random.randint(1,5))
#print(histogram_dataset)
plt.title('Histogram')
plt.xlabel('Numbers')
plt.ylabel('Counts')
plt.hist(histogram_dataset,density=False,color='g')
plt.show()

#3D plotting
axes = plt.axes(projection = '3d')
axes.scatter3D(x,y_1,y_2,marker='^')
axes.set_xlabel('X Axis')
axes.set_ylabel('Y Axis')
axes.set_zlabel('Z Axis')
plt.show()


