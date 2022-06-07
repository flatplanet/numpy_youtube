import numpy as np

list1 = [1,2,3,4,5]
#print(list1)
#print(list1[0])

list2 = ["John Elder", 41, list1, True]
#print(list2)


# Numpy - Numeric Python
# ndarray = n-dimensional array

np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)

# Range
np2 = np.arange(10)
print(np2)

# Step
np3 = np.arange(0,10, 2)
print(np3)

# Zeros
np4 = np.zeros(10)
print(np4)

# Multidimensional zeros
np5 = np.zeros((2,10))
print(np5)

# Full
np6 = np.full((10), 6)
print(np6)

# Multidimensional Full
np7 = np.full((2,10), 6)
print(np7)

# Convert Python lists to np
my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8)

print(np8[0])

