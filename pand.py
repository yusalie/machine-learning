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

# loc
x = data_set.loc['S2']
print(x)

# iloc
y = data_set.iloc[1][3]
print(y)

# filter iloc
filtered_ds = data_set.iloc[:,1:3]
print(filtered_ds)

# dropping column
print(data_set.drop('Grade1',axis=1))

# replacing data in data frame
data_set = data_set.replace(10,12)
print(data_set)

data_set = data_set.replace({12:10,9:15})
print(data_set)

# check first rows
print(data_set.head(3))

# check last rows
print(data_set.tail(2))