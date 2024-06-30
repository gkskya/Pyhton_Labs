import random
import time

def polynomialEv(a, x):
    p = 0.0
    n = len(a)
    for i in range(n-1, -1, -1):
        power = 1
        for j in range(1, i+1):
            power *= x
        p += a[i] * power
    return p

a = [random.randint(0, 100000) for i in range(1000)]

x = 2


total = 0
num = 1000
for i in range(num):
    start = time.time()
    p = polynomialEv(a, x)
    end = time.time()
    total+= (end- start)

avg = total / num
print("Average time taken for {} polynomial evaluations: {:.6f} seconds".format(num, avg))
