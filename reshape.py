# using reshape function
import numpy
array = (list(map(int,numpy.array(input().split()))))
matrix = numpy.reshape(array, (3,3))
print(matrix)

'''
Input 
1 2 3 4 5 6 7 8 9

Output
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
