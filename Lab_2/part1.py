import numpy as np
from collections import Counter

# a. Create and print a 4x2 matrix with values ranging from 2 to 10
arr_a = np.arange(2, 10).reshape(4, 2)
print('Part a: \n', arr_a)
print('\n')

# b. Create and print a 8x8 matrix and fill it with a checkerboard pattern
arr_b = np.zeros((8, 8), dtype = int)
# starting from arr_b[1], jump every 2 rows, make every 2nd integer = 1
arr_b[1::2, ::2] = 1
# starting from arr_b[0], jump every 2 rows, making every 2nd integer = 1 from arr_b[][1]
arr_b[::2, 1::2] = 1
print('Part b: \n', arr_b)
print('\n')

# c. Get the unique values of a list
list_c = [10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
arr_c = np.array(list_c)
counterObj = Counter(list_c)
unique_val = np.unique(arr_c)
print('Part c:')
print(unique_val)
print('\n')


# d. Get the values greater than 37 in the list
list_d = [6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57]
arr_d = np.array(list_d)
print('Part d: ')
print(arr_d[arr_d > 37])
print('\n')

# e. Convert the values of a list of values in Centigrade into Fahrenheit degrees
list_e = [0, 12, 45.21 ,34, 99.91]
C = np.array(list_e)
print('Part e: ')
print(np.round((C * 9/5 + 32), 2))
print('/n')

