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
arr2D = np.zeros((arr1D.shape[0],arr1D.shape[0]), dtype='int32')
print(arr1D)
print(arr2D)
print(arr1D.shape)
for i in range(0,arr1D.shape[0]):
    for j in range(0,arr1D.shape[0]):
        arr2D[i,j]=arr1D[j]-i

print(arr2D)

#QUESTION 3

"""
I was feeling a bit confused about the terms. I was in class but needed a more basic and easy way to understand the 2 methods.
This article helped me understand the question and concepts: https://towardsdatascience.com/stochastic-gradient-descent-clearly-explained-53d239905d31
To answer the question, we save time by using randomness to find the minimum. In the standard method, a random point is selected at first and the step size is found.
Then the new parameters are computed and the process repeats to find the minimum. This requires lots of repeat computations. It is also ideal to have a small step size because if the step is too big,
you risk stepping over the minimum. With the Stochastic method, there is not steps per say, but rather, at every iteration a new point is selected. This prevents the risk of stepping over the min and having to compute parameters and steps every iteration.
The article talks about another methods that combines the speed of the Stochastic method and the precision of the standard method where random points are selected and go though a bit of the standard gradient method.
To be honest, I am still unclear on the details and the core concepts of the different methods, so this is the best I understand the question with some help from the article cited above.
"""
