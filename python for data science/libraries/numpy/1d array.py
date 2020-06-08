import numpy as np

l1 = [1,2,5]
l2 = [4,5,7]

# creating array from the array
a = np.array(l1)

print(a)

# multitplying all the elements at once
print(a*2)

# adding elements of array
print(l1+l2)

# display numbers of elements in array
print(a.size)

# operation on array
# finding elements greater than 10 and less than 50
a = np.array([1,5,9,12,15,7,18,90])
print(a[(a>10) & (a<50)])
