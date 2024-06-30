import math
import time

#find prime numbers less than the value
def sieve_of_eratosthenes(n):
    primes = [True] * n
    primes[0] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i-1]:
            for j in range(i**2, n+1, i):
                primes[j-1] = False
    return [i for i in range(2, n+1) if primes[i-1]]

#find prime factors 
def prime_factorization(n):
    primes = sieve_of_eratosthenes(int(math.sqrt(n)) + 1)
    factors = []
    for p in primes:
        while n % p == 0:
            factors.append(p)
            n = n // p
    if n > 1:
        factors.append(n)
    return factors

#find gcd (middle school procedure)
def middle_school_gcd(m, n):
    m_factors = prime_factorization(m)
    n_factors = prime_factorization(n)
    common_factors = []
    for factor in m_factors:
        if factor in n_factors:
            common_factors.append(factor)
            n_factors.remove(factor)
    gcd = 1
    for factor in common_factors:
        gcd *= factor
    return gcd

def sumOfN(n):
    total=0
    start=time.time()
    for i in range(n+1):
        total+=i
    end=time.time()
    return(total, end-start)

#Main 
m = int(input("Enter n: "))
n = int(input("Enter m: "))
gcd = middle_school_gcd(m, n)
print("GCD", gcd)

start=time.time()
the_sum=100000*(100000+1)/2
end=time.time()
print("Execution time",end-start)
