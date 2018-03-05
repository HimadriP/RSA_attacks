import random

def reiter_attack(ciphers, N, r, e=3):

        P.<x> = PolynomialRing(Zmod(N))
	c1, c2 = ciphers

        g1 = x ^ e - c1
        g2 = (2*x + r) ^ e - c2
                     
        #print(type(g1))

        return -polynomial_gcd(g1,g2).coefficients()[0]

def polynomial_gcd(g1,g2):
         return g1.monic() if g2 == 0 else polynomial_gcd(g2, g1 % g2)

def test():
	N = random_prime(2^50) * random_prime(2^50)
        
	m1 = int("hello".encode("hex"),16)
        print "message 1 = %d" %m1
        r = random.randint(0,N)
	m2 = 2*m1 + r
        print "message 2 = %d" %m2
        
	ciphers = [pow(m1,3,N),pow(m2,3,N)]

	print reiter_attack(ciphers,N,r)

test()
