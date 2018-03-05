
# This file was *autogenerated* from the file reiter.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_16 = Integer(16); _sage_const_50 = Integer(50)
import random

def reiter_attack(ciphers, N, r, e=_sage_const_3 ):

        P = PolynomialRing(Zmod(N), names=('x',)); (x,) = P._first_ngens(1)
	c1, c2 = ciphers

        g1 = x ** e - c1
        g2 = (_sage_const_2 *x + r) ** e - c2
                     
        #print(type(g1))

        return -polynomial_gcd(g1,g2).coefficients()[_sage_const_0 ]

def polynomial_gcd(g1,g2):
         return g1.monic() if g2 == _sage_const_0  else polynomial_gcd(g2, g1 % g2)

def test():
	N = random_prime(_sage_const_2 **_sage_const_50 ) * random_prime(_sage_const_2 **_sage_const_50 )
	
        msg = raw_input("Enter message : ")
	m1 = int(msg.encode("hex"),_sage_const_16 )
	print "the value of N is %d" % N
        print "message 1 = %d" %m1
        r = random.randint(_sage_const_0 ,N)
	m2 = _sage_const_2 *m1 + r
        print "message 2 = %d" %m2
        
	ciphers = [pow(m1,_sage_const_3 ,N),pow(m2,_sage_const_3 ,N)]

	print reiter_attack(ciphers,N,r)

test()

