# 2d array

import numpy as np

# data
a = np.array([ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] ])

print(a)

# dimensions of array
print(a.shape)

# transpose
print(a.transpose())

############## operations on array

# 1st element of every row
print(a[:,0])

# elements greater than 7 in 2nd row
print(a[1][a[1,:]>7])

# array of ones and zeroes
print(np.ones(4,int))
print(np.zeros(4,int))

# array of particular range with steps
print(np.arange(1,10,2))

# reshaping the array
print(a.reshape((5,2)))

# horizontal vs vertical stack
a1 = np.array([1,2,3,4,5])
a2 = np.array([6,7,8,9,10])

print(np.vstack((a1,a2)))
print(np.hstack((a1,a2)))