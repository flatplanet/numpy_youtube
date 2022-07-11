import numpy as np

# Search
np1 = np.array([1,2,3,4,5,6,7,8,9,10, 3])

#x = np.where(np1 == 3)
#print(np1)
#print(x[0])
#print(np1[x[0]])


# Return even items
#y = np.where(np1 % 2 == 0)
#print(np1)
#print(y[0])

# Return odd items
z = np.where(np1 % 2 == 1)
print(np1)
print(z[0])