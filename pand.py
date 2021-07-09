import pandas as pd
import  numpy as np
# series
age = pd.Series([10,20,30,40],index=['age1','age2','age3','age4'])
print(age)

# filter
filtered_age = age[age>20]
print(filtered_age)

# calling the values of the series
print(age.values)

# caliing the indexes of the series
print(age.index)

# DataFrame
df = np.array([[20,1,18],[25,8,10],[27,5,33],[30,9,27]])
print(df)
data_set = pd.DataFrame(df,index=['S1','S2','S3','S4'],columns=['Age','Grade1', 'Grade2'])
data_set['Grade3'] = [9,6,7,10]
print(data_set)