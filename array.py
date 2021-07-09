import numpy as np
from numpy.lib.function_base import median

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(matrix)

matrix2 = np.array([[1,3],[5,7]])

matrix3 = np.array([[2,4],[6,8]])

#multiplying arrays use '@'
print(matrix2@matrix3)

#multiplying usig '*' multiplies each element by the respective element
print(matrix2*matrix3)

#multiplying using dot
print(np.dot(matrix2,matrix3))

#sum of array
print(matrix2+matrix3)

#subtract array
print(matrix2-matrix3)

#division
npDivide = np.divide(matrix2,matrix3)
print(npDivide)

#squareroot
squareRoot = np.math.sqrt(25)
print(squareRoot)

#normal distribution
rndND = np.random.standard_normal((3,4))
print(rndND)
print("")
#uniform distribution
rndUD = np.random.uniform(1,15,(3,4))
print(rndUD)

############################

rndAR = np.random.randint(1,50,(2,5))

filter_ar = np.logical_and(rndAR>30, rndAR<50)
print(filter_ar)
f_ar = rndAR[filter_ar]
print(f_ar)

##############################
data = np.array([1,5,9,6,7,2])
mean_data = np.mean(data)
median_data = np.median(data)
var_data = np.var(data)
sd_data = np.std(data)
print("mean of data: ",mean_data)
print("meadian of data:",median_data)
print("variance of data:", var_data)
print("standard deviation of data:", sd_data)

data2 = np.array([[1,5,6,9],[1,8,6,4]])
var_data2 = np.var(data2, axis=1)
print("variance of data2:", var_data2)
var_data3 = np.var(data2, axis=0)
print("variance of data3:", var_data3)