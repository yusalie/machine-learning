import numpy as np

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