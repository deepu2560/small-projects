import numpy as np
# indexing array

print("indexing in an array")
arr = np.arange(11)

print(arr)
print(arr[2])
print(arr[3:8])
arr[3:8] = 100
print(arr)

print("\n slicing array")
arr = np.arange(11)
slice_arr = arr[:5]

print(slice_arr)
slice_arr[:] = 44
print(slice_arr)
print(arr)

print("\ncoping array")
arr_copy = arr.copy()
print(arr_copy)

print("\nindexing in 2d array")
arr2d = np.array(([1, 2, 3], [5, 6, 7], [33, 44, 55]))

print(arr2d)
print(arr2d[1])
print(arr2d[1][1])
print(arr2d[1]*arr2d[0])
print(arr2d[:2, 1:])

print("\n2d array of zeroes")
arr2d = np.zeros((10, 10))

print(arr2d)

arr_length = arr2d.shape[1]
print(arr_length)

for i in range(arr_length):
    arr2d[i] = 1

print(arr2d)

for i in range(arr_length):
    arr2d[i] = i

print(arr2d)
print(arr2d[[2, 3, 4, 9]])
