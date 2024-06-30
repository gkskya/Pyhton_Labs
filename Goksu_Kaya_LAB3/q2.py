def gcd(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m

m = int(input("Enter first number for GCD: "))
n = int(input("Enter second number for GCD: "))
print("GCD from euclid's", gcd(m, n))
