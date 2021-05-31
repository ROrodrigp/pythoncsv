import numpy as np 
import math 

a = np.array([1,2,3,4])
print(a)
print(a.ndim)


b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.ndim)
print(b.shape)


d = np.zeros(10)
print(d)

e = np.ones((2,3))
print(e)


f = np.arange(1,100,5)
print(f)