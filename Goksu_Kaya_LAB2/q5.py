import time

def sumOfN(n):
    total=0
    start=time.time()
    for i in range(n+1):
        total+=i
    end=time.time()
    return(total, end-start)

#main
print("Sum is %d and time is %10.8f seconds"%sumOfN(100000))

start=time.time()
the_sum=100000*(100000+1)/2
end=time.time()
print("Time is",end-start)