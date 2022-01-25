import numpy as np

#QUESTION 1

a = np.zeros((7,7), dtype='int32')  # Create an array of all zeros , dtype= int
print(a)

print(a.itemsize)

for i in range (0,7):
    for j in range(0,7):
        a[i,j]=j

print(a)

#QUESTION 2

arr1D = np.array([0,1,2]) 
arr2D = np.zeros((3,3), dtype='int32')
print(arr1D)
print(arr2D)
for i in range(0,3):
    for j in range(0,3):
        arr2D[i,j]=arr1D[j]-i

print(arr2D)

#QUESTION 3

"""

"""
