# visualization with matplotlib 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

year = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
ti = [0.72,0.61,0.65,0.68,0.75,0.90,1.02,0.93,0.85,0.99,1.02]

# plot data line graph

plt.rcParams['font.size'] = 6
plt.plot(year,ti)
plt.xlabel("Year")
plt.ylabel("Temperature")
plt.title("Global Warming")

#################################

Month = ['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
customer1 = [12,13,9,8,7,8,8,7,6,5,8,10]
customer2 = [14,15,17,7,6,6,7,6,5,9,12,11]
plt.subplot(3, 4, 1)
plt.plot(Month,customer1, color='red', label='Customer1', marker='o')
plt.plot(Month,customer2, color='blue', label='Customer2', marker='o')
plt.xlabel("Month")
plt.ylabel("Electricity usage")
plt.title("Electricity usage for building")
plt.legend()

plt.subplot(3, 4, 2)
plt.plot(Month,customer1, color='red', label='Customer1', marker='o')
plt.xlabel("Month")
plt.ylabel("Electricity usage")
plt.title("Electricity usage for building for customer1")

plt.subplot(3, 4, 3)
plt.plot(Month,customer2, color='blue', label='Customer2', marker='o')
plt.xlabel("Month")
plt.ylabel("Electricity usage")
plt.title("Electricity usage for building for customer2")

# Scatter plot graph
plt.subplot(3, 4, 4)
plt.scatter(Month, customer1, color='red',label='customer1')
plt.scatter(Month, customer2, color='blue',label='customer2')
plt.xlabel('Month')
plt.ylabel('Electricity usage')
plt.title('Scatter plot of Electricity Usage')
plt.grid()
plt.legend()

# histogram
plt.subplot(3, 4, 5)
plt.hist(customer1, bins=50, color='green')
plt.xlabel('Month')
plt.ylabel('electricity usage')

# Bar chart
plt.subplot(3, 4, 6)
plt.bar(Month, customer1,width=0.8 ,color='blue')
plt.show()