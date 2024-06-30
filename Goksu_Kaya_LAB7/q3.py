def LumutoPartition(A, l, r):
    p = A[l]
    s = l
    for i in range(l+1, r+1):
        if A[i] < p:
            s += 1
            A[s], A[i] = A[i], A[s]
    A[l], A[s] = A[s], A[l]
    return s

arr = [10, 7, 8, 9, 1, 5]
print("The following is the output for the array : ", arr)

n = int(input("Enter the item number that will be searched as index value:"))

pivot = LumutoPartition(arr, 0, len(arr)-1)

while pivot!= n-1:
    if pivot < n-1:
        pivot = LumutoPartition(arr, pivot+1, len(arr)-1)
    else:
        pivot = LumutoPartition(arr, 0, pivot-1)

print(arr)
print(arr[n])
