import numpy as np 
import math

a = np.array([10,20,30,40])
b = np.array([1,2,3,4])


c = a-b 
print(c)


print(a > 19)

A = np.array([[1,6,7],[2,3,6],[5,3,8]])
B = np.array([[5,1,8],[1,34,4],[2,65,2]])
print(A @ B)
print(A.shape)



d = np.random.rand(10)
print(d)
print(d.sum())
print(d.max())
print(d.min())
print(d.mean())

e = d.reshape(2,5)
print(e)