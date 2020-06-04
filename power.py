import numpy as np

a=[
   [2,-1,0],
   [-1,2,-1],
   [0,-1,2]]
n=len(a)
x=np.ones(n)
T=np.zeros(n)

p=np.zeros(n)
count=0
for i in range(10):
	y=np.matmul(a,x)
	x=y/max(y)
	T=abs(x-y)
	if (max(T)!=0 and max(T)<=0.01):
		break
	count+=1	
l=np.matmul(np.matmul(a,x),x)/np.matmul(x,x)
print('The largest eigen value is:',l)		
