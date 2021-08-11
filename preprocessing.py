import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
from IPython.display import display

data_set1 =pd.read_csv('Data_Set.csv')

data_set2 = pd.read_csv('Data_Set.csv',header=2)

data_set3 = data_set2.rename(columns={'Temperature':'Temp'})

data_set4 = data_set3.drop('No. Occupants', axis=1)

data_set5 = data_set4.drop(2,axis=0)

data_set6 = data_set5.reset_index(drop=True)

data_set6_des = data_set6.describe()
print(data_set6_des)

min_item = data_set6['E_Heat'].min()
x = data_set6['E_Heat'][data_set6['E_Heat'] == min_item]
print(min_item)
print(x)
data_set6.replace(-4, 21, inplace=True)

# Covariance
data_cov = data_set6.cov()
print(data_cov)
sn.heatmap(data_cov.corr())
plt.show()

# Missing values
data_set6_info = data_set6.info()
print(data_set6_info)

data_set7 = data_set6.replace('!',np.NaN)

print(data_set7.info())
# displays data set
display(data_set7)