
import time
from Crypto.Util.number import bytes_to_long, long_to_bytes 


def coppersmith_howgrave_univariate(pol, mod, beta, mm, tt, XX):
    
    deg = pol.degree()
    nn = deg * mm + tt

    #ring of pol and x is changed here
    
    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    #here we compute the polynomials according to howgrave univariate
    g = []
    
    for i in range(mm):
        
        for j in range(deg):
            g.append((x * XX)**j * mod**(mm - i) * polZ(x * XX)**i)
    
    for i in range(tt):
        g.append((x * XX)**i * polZ(x * XX)**mm)
    
    
    #construction of lattice B
    
    B = Matrix(ZZ, nn)

    for i in range(nn):
        for j in range(i+1):
            B[i, j] = g[i][j]


    #Using LLL algorithm
    B=B.LLL()

    #transform shortest vector in polynomial    
    
    npol = 0
    for i in range(nn):
        npol += x**i*B[0, i] / XX**i

    #finding roots of the polynomial
    possible_r= npol.roots()

    #testing the correctness of the roots
    root_list = []
    for r in possible_r:
        if r[0].is_integer():
            result = polZ(ZZ(r[0]))
            if gcd(mod, result) >= mod^beta:
                root_list.append(ZZ(r[0]))

	return root_list



kp=raw_input("Enter the known plaintext KP:")
print ""

length_N = 1024  # size of the mod
Kbits = 200      # max size of the root

e = 4

p = next_prime(2^int(round(length_N/2)))
q = next_prime(p)
N = p*q
ZmodN = Zmod(N)
print "Value of N for the demo is", N
print ""
print "Value of e for the demo is", e
print ""


K = Integer(bytes_to_long(kp))
print "The message after conversion to integer is:",K

Kdigits = K.digits(2)
print "The message after conversion to binary is:",Kdigits

#making the message
M = [0]*Kbits + [1]*(length_N-Kbits); 

for i in range(len(Kdigits)):
    M[i] = Kdigits[i]

print "M in binary is:",M
print "\n"

M = ZZ(M, 2) #message completed

#corresponding ciphertext
C = ZmodN(M)^e



print "The value of M is:", M
print "The value of C is:", C

#Forming the equation to be solved
# c=((m+x)^e)mod(n)

known=2^length_N - 2^Kbits #m
print "m:",known

P.<x> = PolynomialRing(ZmodN) 
pol = (known + x)^e - C
deg = pol.degree()

beta = 1                              
eps = beta / 7                      
mm = ceil(beta**2 / (deg * eps))     
tt = floor(deg * mm * ((1/beta) - 1))    
XX = ceil(N**((beta**2/deg) - eps))  


roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)

print "The roots of the Coppersmith Howgrave-Graham algorithm are ",roots
print "Original message:",str(K)
print "The roots obtained:", str(roots)
print "\n"
message=long_to_bytes(int(''.join(map(str,roots))))
print "Original message is:",message


