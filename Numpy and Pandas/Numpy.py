                                   # EXERCISES 

import numpy as np

# 1. Create two dimensional 3*3 array and perform ndim, shape, slicing operation on it.

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D Array:\n", arr2d)
print("ndim:", arr2d.ndim)
print("shape:", arr2d.shape)
print("slicing arr2d[0:2, 1:3]:\n", arr2d[0:2, 1:3])


# 2. Create one dimensional array and perform ndim,shape, reshape  operation on it.

arr1d = np.array([10,20,30,40,50,60])
print("\n1D Array:", arr1d)
print("ndim:", arr1d.ndim)
print("shape:", arr1d.shape)
reshaped = arr1d.reshape(2,3)
print("Reshaped 2x3 array:\n", reshaped)