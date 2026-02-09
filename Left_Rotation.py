def rotateLeft(d, arr):
    # Write your code here
    n= len(arr)
    arr= arr+arr
    return arr[d:d+n]

print(rotateLeft(4, [1, 2, 3, 4, 5]))

