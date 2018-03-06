import random
# to generate random prime numbers


def gcd_of_pol(g,h):
    return g.monic() if h == 0 else gcd_of_pol(h, g % h)


def reiter(ciphertxt, N, r, e):

    P.<x> = PolynomialRing(Zmod(N))
	c1, c2 = ciphertxt

    g = x ^ e - c1
    h = (2*x + r) ^ e - c2

    result = gcd_of_pol(g,h).coefficients()[0]
    result1 = -result

    return result1


# modulus N is a product of two large prime numbers p and q
p = random_prime(2^50)
q = random_prime(2^50)
N = p * q
    
m1=raw_input("Enter message to be transmitted:")

m1 = int(m1.encode("hex"),16)

e=raw_input("Enter public key exponent e:")

print "Message-1 = %d" %m1

r = random.randint(0,N)

m2 = 2*m1 + r #making a related message
print "Message-2 = %d" %m2
        
ciphertxt = [pow(m1,e,N),pow(m2,e,N)]

print reiter(ciphertxt,N,r,e)

