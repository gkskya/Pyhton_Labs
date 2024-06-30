import random
import time

arr = [random.randint(0, 100) for i in range(1000)]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

start = time.time()
bubbleSort(arr)
end = time.time()


print(arr)
print(end - start)

