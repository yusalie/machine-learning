# visualization with matplotlib 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

year = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
ti = [0.72,0.61,0.65,0.68,0.75,0.90,1.02,0.93,0.85,0.99,1.02]

# plot data line graph
plt.plot(year,ti)
plt.xlabel("Year")
plt.ylabel("Temperature")
plt.title("Global Warming")
plt.show()

#################################

Month = ['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
customer1 = [12,13,9,8,7,8,8,7,6,5,8,10]
customer2 = [14,15,17,7,6,6,7,6,5,9,12,11]

plt.plot(Month,customer1, color='red', label='Customer1', marker='o')
plt.plot(Month,customer2, color='blue', label='Customer2', marker='o')
plt.xlabel("Month")
plt.ylabel("Electricity usage")
plt.title("Electricity usage for building")
plt.legend()
plt.show()

plt.subplot()