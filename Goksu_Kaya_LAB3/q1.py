def gcd(m, n):
    t = min(m, n)
    while t > 0:
        if m % t == 0 and n % t == 0:
            return t
        t -= 1

m = int(input("A non-negative integer please: "))
n = int(input("Another non-negative integer please: "))
print("GCD from consecutive check", gcd(m, n))
