import numpy as np
A=np.array([[3,1,0],[1,3,1],[0,1,3]])
q,r=np.linalg.qr(A)
print(q)
print(r)
print(np.linalg.eigh(A))
	
	

