import random
import time

arr = [random.randint(0, 100) for i in range(1000)]

def sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for k in range(i+1, len(arr)):
            if arr[k] < arr[min_ind]:
                min_ind = k
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


start = time.time()
sort(arr)
end = time.time()


print(arr)
print(end - start)



