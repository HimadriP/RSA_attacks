import random
import math

def gcd(a,b):
    if a<=0:
        return b
    return gcd(b%a,a)

def rho(number,x,y):
    d = 1
    while d is 1:
        x = (x**2+1)%number
        for i in range(0,2,1):
            y = (y**2+1)%number
        if x>y:
            z = x-y
        else:
            z=y-x
        d = gcd(z,number)
    return d

def factorize(n):
    #initialising x and y values
    x=2
    y=2

    factor1 = rho(n,x,y)
    while factor1 is  1:
        x = x+1
        y = y+1
        factor1 = rho(n,x,y)
    factor2 = int(n/factor1)
    return factor2,factor1

n = input("Enter the number n :")

p,q = factorize(n)
print "The Two Factors are : %i and %i" % (p,q)
