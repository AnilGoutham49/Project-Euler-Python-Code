# def prime_fac(n):
#     p = int(n/6)
#     f1 = lambda k: 6*k+1
#     f2 = lambda k: 6*k+5
#     primes = [f(k) for k in range(1,p+1) for f in (f1,f2)]
#     factors = [x for x in primes if n%x == 0]
#     return f'The prime factors are: {factors}'
#
# print(prime_fac(13195))

#solution from geeksforgeeks
import math
def prime_fac(n):
    maxP = -1

    while n%2==0:
        maxP = 2
        n /= 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n%i==0:
            maxP = i
            n = n/i

    if n>2:
        maxP = n

    return int(maxP)

print(prime_fac(600851475143))
