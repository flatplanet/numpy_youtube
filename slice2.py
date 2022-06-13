import numpy as np

# Slicing

np1 = np.array([1,2,3,4,5,6,7,8,9])
# Return 2,3,4,5
print(np1[1:5])  # Start to up to finish

# Return from something till end
# Returns 4-9
print(np1[3:])

# Negative Slicing count from end backwards
# Return 7, 8
print(np1[-3:-1])

# Return Steps
print(np1[1:5])
print(np1[1:5:2])

# Step the entire array:
print(np1[::2]) 
print(np1[::3])

# Grabbing Item from 2-d Arrays
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# Return 8
print(np2[1,2])

# Slicing 2-d Array
# you need to specify both a row index 
# and a column index as 
# [row_index, column_index].
# [start_row_index:end_row_index, start_column_index:end_column_index]
# Return 2,3
print(np2[0:1, 1:3])

# Return 2,3 and 7,8
print(np2[0:2, 1:3])





