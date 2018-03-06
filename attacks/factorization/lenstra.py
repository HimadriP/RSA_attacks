from fractions import gcd

from random import randint

# Prime number generator ( Sieve )
def sieve(n):
    filter = [True] * (n + 1)
    primes = []
    for p in xrange(2, n + 1):
        if filter[p]:
            primes.append(p)
            for i in xrange(p, n + 1, p):
                filter[i] = False
    return primes

# Modular multiplicative inverse
def inverse_mult(a, b):
    if b == 0:
        return 1, 0, a
    q, r = divmod(a, b)
    x, y, g = inverse_mult(b, r)
    return y, x - q * y, g

# Elliptic curve addition in modulo m space
def eladd(p, q, a, b, m):
    # if p or q = infinity, r = q or p
    if p[2] == 0:
        return q
    if q[2] == 0:
        return p
    if p[0] == q[0]:
        #if point of infinity
        if (p[1] + q[1]) % m == 0:
            return 0, 1, 0

        #numerator and denominator for the slope of the line
        numerator = (3 * p[0] * p[0] + a) % m
        denominator = (2 * p[1]) % m
    else:
        numerator = (q[1] - p[1]) % m
        denominator = (q[0] - p[0]) % m
    inv, _, g = inverse_mult(denominator, m)
    # elliptic arithmetic breaks if inverse does not exist
    if g > 1:
        return 0, 0, denominator

    #Calculating the value of x and y at R
    z = (numerato * inv * numerator * inv - p[0] - q[0]) % m
    return z, (numerator * inv * (p[0] - z) - p[1]) % m, 1


# Elliptic multiplication using doubling(repeated addtion -> p + p) [ on mod m ]
def elmult(k, p, A, B, m):
    #Infinity Point
    r = (0, 1, 0)
    while k > 0:
        # If point P is failing return answer
        if p[2] > 1:
            return p
        if k % 2 == 1:
            r = eladd(p, r, A, B, m)
        k = k // 2
        p = eladd(p, p, A, B, m)
    return r

# Lenstra's algorithm for factoring
def lenstra(n, limit=1000):
    d = n
    while d == n:
        # Randomly selecting the points x and y
        xq = randint(0, n - 1)
        yq = randint(0, n - 1)
        q = xq,yq,1
        # Randomly selecting curve coeff 
        A = randint(0, n - 1)
        B = (q[1] * q[1] - q[0] * q[0] * q[0] - A * q[0]) % n
        # singularity check
        d = gcd(4 * A * A * A + 27 * B * B, n)  

    if d > 1:
        return d
    # Incrementing the numeber K till lcm(1, ..., limit)
    for p in sieve(limit):
        k = p
        while k < limit:
            q = elmult(p, q, A, B, n)
            # Elliptic arithmetic breaks, The
            if q[2] > 1:
                factor1 = gcd(q[2],n)
                factor2 = n/factor1
                return "Factors are : %i and %i" % (factor1,factor2)
            k = p * k
            
    return "The number itself is a prime number"

n = input("Enter the number n:")   
print lenstra(n)

