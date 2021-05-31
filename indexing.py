import numpy as np
import math

a = np.array([1,4,5,2])
print(a[3])



A = np.array([[1,2],[3,4],[5,6]])
print(A)
print(A[1,1])
B = np.array([A[0,0],A[1,1],A[2,1]])
print(B)
C = (A[[0,1,2],[0,1,1]])
print(C)