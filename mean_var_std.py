import numpy
numpy.set_printoptions(sign=' ')

n,m=map(int,input().split())
arr=numpy.array([input().split() for _ in range(n)],int)

print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
std=numpy.std(arr,axis=None)
print(numpy.around(std,decimals=12))
