#for 循环
L=[[1,2,3],[4,5,6],[7,8,9]]

print([[j[i] for j in L] for i in range(len(L[0]))])

#zip 函数
l = []
for s in zip(*L):
	l.append(list(s))
print(l)	

#numpy 库
import numpy as np

L = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(L.T)
print(L.transpose())
	

