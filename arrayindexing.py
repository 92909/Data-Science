import numpy as np

# Accessing array elements is the same as array indexing
# you can access an array element by refering to its index on the array
# As always, arrays start at index 0

arra1 = np.array([1, 3, 23, 43, 56])
print(arra1[0])

# accessing 2-D arrays
arra2 = np.array([[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]])
print(arra2[0,1])

# lets try adding different arrays
print(arra1[1] + arra2[1,2])

# accessing 3-d arrays
arra3 = np.array([[[31, 32, 33, 34, 35], [36,37,38,39,40]], [[41,42,43,44,45], [46,47,48,49,50]]])
print(arra3[0,1,2])