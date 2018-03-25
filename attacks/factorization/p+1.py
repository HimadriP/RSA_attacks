#!/usr/bin/env python2.7

from math import sqrt
from itertools import count

def gcd(a, b):
    while b: a, b = b, a%b
    return abs(a)

def generator_for_primes():
    #Sieve of eratosthenes to generate primes
    yield 2; yield 3; yield 5; yield 7; yield 11; yield 13
    ps = generator_for_primes() # yay recursion
    p = ps.next() and ps.next()
    q, sieve, n = p**2, {}, 13
    while True:
        if n not in sieve:
            if n < q: yield n
            else:
                next, step = q + 2*p, 2*p
                while next in sieve: next += step
                sieve[next] = step
                p = ps.next()
                q = p**2
        else:
            step = sieve.pop(n)
            next = n + step
            while next in sieve: next += step
            sieve[next] = step
        n += 2
 
def lucas_seq_modm(v, a, n):
    
    v1, v2 = v, (v**2 - 2) % n
    #Finding the mth element of the bits
    for bit in bin(a)[3:]:
        v1, v2 = ((v1**2 - 2) % n, (v1*v2 - v) % n) if bit == "0" else ((v1*v2 - v) % n, (v2**2 - 2) % n)
    return v1

def ilog(x, b):
    # greatest integer l such that b**l <= x.
    l = 0
    while x >= b:
        x /= b
        l += 1
    return l

def williams_pp1(n):
    #Regularly increment v from 1 -- ie: 1,2,3,4,5..
    for v in count(1):
        #Generate primes 
        for p in generator_for_primes():

            e = ilog(sqrt(n), p)
            if e == 0:
                break
            
            #Using Lucas sequences 
            for _ in xrange(e):
                v = lucas_seq_modm(v, p, n)

            print("The value of v generated from lucas sequence is : ",v)
            factor = gcd(v - 2, n)

            # If g is a factor
            if 1 < factor < n:
                return factor
            if factor == n:
                break

if __name__=="__main__":
    n = input("Enter the value of n:")
    factor1 = williams_pp1(n)
    factor2 = n/factor1
    print("The factors of %d are %d and %d" % (n,factor1,factor2))
    
