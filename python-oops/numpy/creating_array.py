import numpy as np

# creating an array

# creating a array from a list
list1 = [1, 2, 3, 4, 5]
arr1 = np.array(list1)

print("array one:\n", arr1)

# creating a matrix array from a matrix list
list2 = [73, 56, 34, 82, 24]
list2d = [list1, list2]
arr2 = np.array(list2d)

print("\n2d array:\n", arr2)
print(arr2.shape)
print(arr2.dtype)

# array of zeros
arr_zeros = np.zeros(5)

print("\narray of zeros having floating number:\n", arr_zeros)

# 2d array of 1s
arr2d = np.ones([2, 5])

print("\n2d array of ones having floating number:\n", arr2d)

# empty array
empty_arr = np.empty(5)

print("\nempty array having datatype of floating numbers:\n", empty_arr)

# identity matrix array
id_arr = np.eye(5)

print("\nan identity matrix array:\n", id_arr)

# creating a array like range method
simple_arr = np.arange(5)

print("\nsimple array from 0 to 5: \n", simple_arr)

advnc_arr = np.arange(5, 50, 2)

print("\narray from 5 to 50 having 2 steps\n", advnc_arr)
