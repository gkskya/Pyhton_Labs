import random
import time

def polynomialEval(a, x):
    p = a[0]
    power = 1
    for i in range(1,len(a)):
        power *= x
        p += a[i] * power
    return p

arr = [random.randint(0, 100000) for i in range(1000)]

x = 2

start = time.time()
result = polynomialEval(arr, x)
end = time.time()

print(result,"\n")
print(end - start, "seconds")

