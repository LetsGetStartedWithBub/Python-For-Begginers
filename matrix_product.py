import numpy

num_of_input=int(input())

a=numpy.array([list(map(int,input().split())) for _ in range(num_of_input)])
b=numpy.array([list(map(int,input().split())) for _ in range(num_of_input)])


print(numpy.dot(a,b))
