import random
import time

def insertionSort(arr):
    for i in range(1, len(arr)):
        v = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v

arr = [random.randint(0, 100000) for _ in range(10000)]

start= time.time()
insertionSort(arr)
end = time.time()

print("Some part of the array", arr[:10])
print("Seconds", end- start)
