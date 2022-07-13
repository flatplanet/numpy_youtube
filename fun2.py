import numpy as np

# Copy Vs. View
np1 = np.array([0,1,2,3,4,5,6,7,8,9])

'''
# Create View of np1
np2 = np1.view()
print(f'Original np1: {np1}')
print(f'Original np2: {np2}')

np1[0] = 41

print(f'Changed np1: {np1}')
print(f'Original np2: {np2}')

# Make a change to the view, the original changes too!
np2[0] = 27
print(f'Changed np2: {np2}')
print(f'np1: {np1}')
'''

# Make a copy
np2 = np1.copy()

print(f'Original np1: {np1}')
print(f'Original np2: {np2}')

np1[0] = 41

print(f'Changed np1: {np1}')
print(f'Original np2: {np2}')

# Make a change to the view, the original changes too!
np2[0] = 27
print(f'Changed np2: {np2}')
print(f'np1: {np1}')


