import numpy
n=int(input())
a = numpy.array([input().split() for _ in range(n)], int) #takes 2 lines of integers for Matrix A
b = numpy.array([input().split() for _ in range(n)], int) #takes 2 lines of integers for Matrix B
print(numpy.matmul(a,b))

'''
Input
2
1 2 
3 4
1 2
3 4

Output
[[ 7 10]
 [15 22]]
'''