#solving a set of linear equations using python library

import numpy as np

A=np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]])
B=np.array([2,2,2])
x=np.linalg.solve(A,B)
print(x)




