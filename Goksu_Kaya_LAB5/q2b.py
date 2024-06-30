import random
import time

arr = [random.randint(0, 100) for i in range(1000)]

def bubble_sort(arr):
    n = len(arr)
    swap = True
    while swap:
        swap = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True

start = time.time()
bubble_sort(arr)
end= time.time()


print(arr)
print(end- start)
