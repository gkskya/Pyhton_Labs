import random
import time


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    l = mergeSort(arr[:middle])
    r = mergeSort(arr[middle:])
    return merge(l, r)

def merge(l, r):
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    return result

arr = [random.randint(1, 1000) for _ in range(10000)]


start = time.time()
sorted= mergeSort(arr)
end= time.time()


print(end - start, "seconds")
print("[",sorted,"]")

