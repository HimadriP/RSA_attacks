import random
import math

#Basic GCD code
def gcd(a,b):
    if a<=0:
        return b
    return gcd(b%a,a)

def rho(number,p,q):
    d = 1
    while d is 1:
        
        #Function choosen is f(a) = (a**2 + 1) mod m
        p = (p**2+1)%number
        for i in range(0,2,1):
            q = (q**2+1)%number
            
        if p>q:
            diff = p-q
        else:
            diff=q-p
        #Getting the factor
        d = gcd(diff,number)
    return d

def factorize(n):
    #initialising x and y values
    x=2
    y=2

    factor1 = rho(n,x,y)
    factor2 = int(n/factor1)
    return factor2,factor1

n = input("Enter the number n :")

p,q = factorize(n)
print "The Two Factors are : %i and %i" % (p,q)
